<template>
    <form action="/searh-query/" method="GET" id="search-form" class="mt-3">
        <!-- <h3>time_ranges</h3>
        {{ time_ranges }} -->

        <nav id="search-form__services-nav" class="mb-3">
            <a v-for="(item, index) in services_navigation"
                :key="item.id"
                :class="{ active : item.active }"
                :data-index="index"
                @click="navItem"
                href="">{{ item.name }}</a>
        </nav>

        <div id="search-form__tiles">
            <div class="search-tiles-group">
                <div class="search-tiles-group__place-date-time">
                    <div class="search-tile st-1">
                        <label for="">Местоположение или салон</label>
                        <select name="city"
                                v-model="city_selected"
                                id="search-tile-input__place"
                                class="search-tile-input search-tile-input__place">
                            <option value="">- Выберите город -</option>
                            <option v-for="(item, index) in cities"
                                    :key="index"
                                    :data-city-id="item.id"
                                    :value="item.name">{{ item.name }}</option>
                        </select>
                    </div>
                    <div class="search-tile st-2">
                        <label for="">Дата визита</label>
                        <datepicker :monday-first="true"
                                    :language="languages[language]"
                                    :input-class="['search-tile-input', 'search-tile-input__date']"
                                    v-model="today"
                                    name="date_of_visit"
                                    format="dd.MM.yyyy (D)"></datepicker>
                    </div>
                    <div class="search-tile st-3">
                        <div>
                            <label for="">Время начала</label>
                            <!-- <input type="time" name="" id="search-tile-input__time" class="search-tile-input search-tile-input__time"> -->
                            <div v-if="!time_certain_checked" id="search-form__time-ranges">
                                <select name="time_start"
                                    v-model="time_start"
                                    id="search-tile-input__time--start"
                                    class="search-tile-input search-tile-input__time">
                                    <option v-for="(item, index) in time_ranges"
                                            :key="index"
                                            :value="item.time">{{ item.time }}</option>
                                </select>
                                <select name="time_end"
                                    v-model="time_end"
                                    id="search-tile-input__time--end"
                                    class="search-tile-input search-tile-input__time">
                                    <option v-for="(item, index) in time_ranges"
                                            :key="index"
                                            :value="item.time">{{ item.time }}</option>
                                </select>
                            </div>
                            <div v-if="time_certain_checked">
                                <select name="time_certain"
                                    v-model="time_certain"
                                    id="search-tile-input__time"
                                    class="search-tile-input search-tile-input__time">
                                    <option v-for="(item, index) in time_ranges"
                                            :key="index"
                                            :value="item.time">{{ item.time }}</option>
                                </select>
                            </div>
                        </div>
                        <div class="mt-2 text-right">
                            <label for="st-precice-time">
                                <input type="checkbox" id="st-precice-time" v-model="time_certain_checked"> точное время
                            </label>
                        </div>
                    </div>
                </div>

                <div class="clone-wrapper">
                    <div v-for="(service_to_add, index) in services_added"
                        :key="index"
                        class="toClone">
                        <div class="search-tiles-group__add-service-wrap">
                            <div class="search-tile st-4">
                                <label for="">Выберите услугу</label>
                                <!-- check if last -->
                                <span v-if="index == services_added.length - 1">
                                    <select name="service_to_add[]"
                                        v-model="service_to_add.id"
                                        id="search-tile-input__services"
                                        class="search-tile-input search-tile-input__services">

                                        <option value="">- Выберите услугу -</option>
                                        <option v-for="(item, index) in services_last"
                                            :key="index"
                                            :value="item.id">{{ item.name }}</option>
                                    </select>
                                </span>
                                <span v-else>
                                    <select name="service_to_add[]"
                                        v-model="service_to_add.id"
                                        id="search-tile-input__services"
                                        class="search-tile-input search-tile-input__services">

                                        <option value="">- Выберите услугу -</option>
                                        <option v-for="(item, index) in services_all"
                                                :key="index"
                                                :value="item.id">{{ item.name }}</option>
                                    </select>
                                </span>

                                <div class="mt-3 text-right text-danger"
                                    v-if="index != 0"
                                    @click.prevent="removeService(index)"
                                    style="cursor: pointer;">X remove</div>
                            </div>
                            <div class="search-tile st-5" @click="addService">
                                <div class="search-tile__add-service">
                                    <div class="search-tile__add-service-plus">+</div>
                                    <div class="search-tile__add-service-text">добавить еще услугу из другой категории?</div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>

        <div v-if="searchQuery" class="text-center mt-3">
            <div class="h4">Вы ищите:</div>
            <div class="search-query">{{ searchQuery }}</div>
        </div>

        <div id="search-form__submit" class="mt-3">
            <button type="submit" @:click="sumbitSearchForm">Начать поиск</button>
        </div>
    </form>
</template>

<script>
import Vue from 'vue';
import axios from "axios";

import Datepicker from 'vuejs-datepicker';
import * as lang from "vuejs-datepicker/src/locale";


export default {
    data() {
        return {
            api_services_url: '/api/services/',
            api_cities_url: '/api/cities/',

            // vuejs-datepicker language, initial date
            language: "ru",
            languages: lang,
            today: new Date(),

            services_navigation: [],
            services_all: [],
            services_last: [],
            services: [],

            services_group_active_id: '',
            services_selected: [],

            service_to_add: {
                "id": '',
                // "name": '',
            },
            services_added: [],

            time_ranges: [],
            time_certain_checked: false,
            time_start: '09:00',
            time_end: '10:30',
            time_certain: '11:00',

            cities: [],
            city_selected: '',
        }
    },

    components: {
        Datepicker,
    },

    mounted() {
        // Set start/end time
        const todayHours = this.today.getHours();

        this.time_start = `${todayHours + 1}:00`;
        this.time_end = `${todayHours + 2}:00`;

        // Set time_certain
        this.time_certain = `${todayHours + 1}:00`;

        // services
        axios
            .get(this.api_services_url)
            .then(res => {
                this.services = res.data;
                // console.log("axios mounted: services", this.services);
            }),

        // services_navigation
        axios
            .get(this.api_services_url)
            .then(res => {
                this.services_navigation = res.data;
                this.fillServicesNavigation(this.services_navigation);
                // console.log("axios mounted: services_navigation", this.services_navigation);
            }),

        // services_all
        axios
            .get(this.api_services_url)
            .then(res => {
                let serv_all_tmp = res.data;
                this.fillServicesAll(serv_all_tmp);
                // console.log("axios mounted: services_all", this.services_all);
            }),

        // cities
        axios
            .get(this.api_cities_url)
            .then(res => {
                this.cities = res.data;
            }),

        // Fill first services_added
        this.services_added.push({'id': ''});

        this.services_last = this.services_all;

        this.generateTimeRanges();
    },

    computed: {
        searchQuery() {
            let added_services = [];
            this.services_added.forEach(el => {
                // get by id services name
                for (let i = 0; i < this.services_all.length; i++) {
                    if (el.id == this.services_all[i].id) {
                        added_services.push(this.services_all[i].name);
                    }
                }
            });

            added_services = added_services.toString();
            let new_added_services = '';
            if (added_services.length > 1) {
                new_added_services = added_services.replace(/,/g, ' + ')
            }

            const city_selected = () => {
                if (this.city_selected != '') {
                    return `, в ${this.city_selected}`;
                } else {
                    return '';
                }
            }

            const time_ranges_formated = () => {
                return `, начало с ${this.time_start} до ${this.time_end}`;
            }

            const time_certain_formated = () => {
                return `, время ${this.time_certain}`;
            }

            if (new_added_services && this.time_certain_checked == false) {
                return `${new_added_services}${city_selected()}${time_ranges_formated()}`;
            }
            if (new_added_services && this.time_certain_checked == true) {
                return `${new_added_services}${city_selected()}${time_certain_formated()}`;
            }
        },
    },

    methods: {
        fillServicesNavigation(services_arr) {
            for (let i = 0; i < services_arr.length; i++) {
                services_arr[i].active = false;
                delete services_arr[i].services;
            }
        },
        fillServicesAll(services_arr) {
            for (let i = 0; i < services_arr.length; i++) {
                if (services_arr[i].services.length > 0) {
                    services_arr[i].services.forEach(el => {
                        this.services_all.push(el);
                    });
                }
            }
        },

        navItem(e) {
            e.preventDefault();

            const index = e.target.getAttribute('data-index');
            this.services_navigation.forEach(el => {
                el.active = false;
            });
            this.services_navigation[index].active = true;

            // Set active services
            this.services_group_active_id = this.services_navigation[index].id;
            if (typeof this.services_group_active_id == "number") {
                this.services.forEach(el => {
                    if (el.id == this.services_group_active_id) {
                        this.services_last = el.services;
                        // console.log(el.services);
                    }
                });
            }

            // console.log(this.$el);
            this.$forceUpdate();
        },

        addService(e) {
            e.preventDefault();

            const index = e.target.getAttribute('data-index');

            this.services_added.push(Vue.util.extend({}, this.service_to_add));
            // this.services_added.push({'name': 'test 111'});
        },
        removeService(index) {
            // console.log('removeService()', index);
            // delete this.services_added[index];
            // this.$forceUpdate();
            Vue.delete(this.services_added, index);
            // console.log(this.services_added);
        },

        generateTimeRanges() {
            let hour = 0;
            let minutes = 0;
            for(let i = 0; i < 24; i++) {
                const time_formated = (hour, minutes) => {
                    if (hour <= 9) {
                        hour = `0${hour}`;
                    }
                    if (minutes <= 9) {
                        minutes = `0${minutes}`;
                    }
                    return `${hour}:${minutes}`;
                }

                if (hour >= 9 && hour <= 21) {
                    this.time_ranges.push({'time': time_formated(hour, minutes)});
                    for(let k = 0; k < 3; k++) {
                        minutes = minutes += 15;
                        this.time_ranges.push({'time': time_formated(hour, minutes)});
                    }
                }

                minutes = 0;
                hour++;
            }
        },

        sumbitSearchForm(e) {
            // e.preventDefault();

            // console.log(this.$data);

            console.log("sumbitSearchForm()");
            // console.log("city_selected:", this.city_selected);
            // console.log("today:", this.today);
            // console.log("time_start:", this.time_start);
            // console.log("time_end:", this.time_end);
            // console.log("services_added:", this.services_added);
        },
    },
}
</script>

<style lang="scss" scoped>
#search-form__time-ranges {
    display: grid;
    grid-gap: 10px;
    grid-template-columns: repeat(2, 1fr);
}

.clone-wrapper {
    display: grid;
    grid-gap: 10px;

    .toClone {
        .search-tiles-group__add-service-wrap {
            display: grid;
            grid-gap: 10px;
            grid-template-columns: repeat(3, 1fr);
            transition: opacity ease-in-out .3s;

            &:hover {
                opacity: .8;
            }

            .st-4 {
                grid-column-start: 1;
                grid-column-end: 3;
            }
        }
    }
}
</style>