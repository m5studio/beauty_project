<template>
    <form id="search-form" class="mt-3">
        <!-- <h3>services</h3>
        {{ services }} -->

        <!-- <h3>services_navigation</h3>
        {{ services_navigation }}
        <br><br> -->

        <!-- <h3>{{ services_group_active_id }}</h3> -->

        <!-- <h3>services_all</h3>
        {{ services_all }} -->

        <h3>time_ranges</h3>
        {{ time_ranges }}

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
                        <select name="" id="search-tile-input__place" class="search-tile-input search-tile-input__place">
                            <option>- Выберите город -</option>
                            <option>Город</option>
                        </select>
                    </div>
                    <div class="search-tile st-2">
                        <label for="">Дата визита</label>
                        <datepicker :monday-first="true"
                                    :language="languages[language]"
                                    :input-class="['search-tile-input', 'search-tile-input__date']"
                                    v-model="today"
                                    format="d MMMM yyyy"></datepicker>
                    </div>
                    <div class="search-tile st-3">
                        <div>
                            <label for="">Время начала</label>
                            <!-- <input type="time" name="" id="search-tile-input__time" class="search-tile-input search-tile-input__time"> -->
                            <select name=""
                                id="search-tile-input__time"
                                class="search-tile-input search-tile-input__time">
                                <option v-for="(item, index) in time_ranges"
                                        :key="index"
                                        :value="item.time">{{ item.time }}</option>
                            </select>
                        </div>
                        <div class="mt-2 text-right">
                            <label for="st-precice-time">
                                <input type="checkbox" name="" id="st-precice-time"> точное время
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
                                    <select name=""
                                        v-model="service_to_add.name"
                                        id="search-tile-input__services"
                                        class="search-tile-input search-tile-input__services">

                                        <option value="">- Выберите услугу -</option>
                                        <option v-for="item in services_last"
                                            :key="item.id"
                                            :value="item.name">{{ item.name }}</option>
                                    </select>
                                </span>
                                <span v-else>
                                    <select name=""
                                        v-model="service_to_add.name"
                                        id="search-tile-input__services"
                                        class="search-tile-input search-tile-input__services">

                                        <option value="">- Выберите услугу -</option>
                                        <option v-for="item in services_all"
                                                :key="item.id"
                                                :value="item.name">{{ item.name }}</option>
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

        <div class="text-center my-3">
            <div class="h4">Вы ищите:</div>
            <div class="search-query">{{ searchQuery }}</div>

            <!-- TODO: remove: -->
            <div class="search-query" style="opacity: .3;">Классический маникюр + Ремонт 1 ногтя + Коррекция бровей в Москве, начало с 09:00 до 12:00</div>
        </div>

        <div id="search-form__submit">
            <button type="submit">Начать поиск</button>
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
            // api_cities_url: '/api/cities/',

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
                "name": '',
            },
            services_added: [],

            time_ranges: [],
        }
    },

    components: {
        Datepicker,
    },

    mounted() {
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

        this.services_added.push({'id': '', 'name': ""});
        this.services_last = this.services_all;

        this.generateTimeRanges();
    },

    computed: {
        searchQuery() {
            let added_services = [];
            this.services_added.forEach(el => {
                added_services.push(el.name);
            });
            // console.log(added_services);

            added_services = added_services.toString();
            let new_added_services = '';
            if (added_services.length > 1) {
                new_added_services = added_services.replace(/,/g, ' + ')
            }

            return `${new_added_services}`;
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

            // console.log('addService()');

            const index = e.target.getAttribute('data-index');
            this.services_added.push(Vue.util.extend({}, this.service_to_add));

            // console.log(this.services_added);
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
            for(let i = 0; i < 24; i++) {
                const hour_fornated = (hour) => {
                    if (hour <= 9) {
                        return `0${hour}:00`;
                    } else {
                        return `${hour}:00`;
                    }
                }

                if (hour >= 8 && hour <= 22) {
                    this.time_ranges.push({'time': hour_fornated(hour)});
                }

                hour++;
            }
        },
    },
}
</script>

<style lang="scss" scoped>
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