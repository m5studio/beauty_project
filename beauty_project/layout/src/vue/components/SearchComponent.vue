<template>
    <form id="search-form" class="mt-3">
        <!-- <h3>services</h3>
        {{ services }} -->

        <h3>services_navigation</h3>
        {{ services_navigation }}
        <br><br>

        <!-- <h3>services_all</h3>
        {{ services_all }} -->

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
                            <input type="time" name="" id="search-tile-input__time" class="search-tile-input search-tile-input__time">
                        </div>
                        <div class="mt-2 text-right">
                            <label for="st-precice-time">
                                <input type="checkbox" name="" id="st-precice-time"> точное время
                            </label>
                        </div>
                    </div>
                </div>

                <div class="clone-wrapper">
                    <!-- <div class="toClone">
                        <div class="search-tiles-group__add-service-wrap">
                            <div class="search-tile st-4">
                                <label for="">Выберите услугу</label>
                                <select name=""
                                    v-model="service_to_add.name"
                                    id="search-tile-input__services"
                                    class="search-tile-input search-tile-input__services">
                                    <option>- Выберите услугу -</option>
                                    <option v-for="item in services_all"
                                        :key="item.id"
                                        :value="item.name">{{ item.name }}</option>
                                </select>
                            </div>
                            <div class="search-tile st-5" @click="addService">
                                <div class="search-tile__add-service">
                                    <div class="search-tile__add-service-plus">+</div>
                                    <div class="search-tile__add-service-text">добавить еще услугу из другой категории?</div>
                                </div>
                            </div>
                        </div>
                    </div> -->

                    <div v-for="(service_to_add, index) in services_added"
                        :key="index"
                        class="toClone">
                        <div class="search-tiles-group__add-service-wrap">
                            <div class="search-tile st-4">
                                <label for="">Выберите услугу</label>

                                <select name=""
                                    v-model="service_to_add.name"
                                    id="search-tile-input__services"
                                    class="search-tile-input search-tile-input__services">

                                    <option value="">- Выберите услугу -</option>

                                    <option v-for="item in services_all"
                                        :key="item.id"
                                        :value="item.name">{{ item.name }}</option>
                                </select>
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
            <div class="search-query">Классический маникюр + Ремонт 1 ногтя + Коррекция бровей в Москве, начало с 09:00 до 12:00</div>
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
            services: [],

            service_to_add: {
                "id": '',
                "name": '',
            },
            services_added: [],
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
                console.log("axios mounted: services", this.services);
            }),

        // services_navigation
        axios
            .get(this.api_services_url)
            .then(res => {
                this.services_navigation = res.data;
                this.fillServicesNavigation(this.services_navigation);
                console.log("axios mounted: services_navigation", this.services_navigation);
            }),

        // services_all
        axios
            .get(this.api_services_url)
            .then(res => {
                let serv_all_tmp = res.data;
                this.fillServicesAll(serv_all_tmp);
                console.log("axios mounted: services_all", this.services_all);
            }),

        this.services_added.push({'id': '', 'name': ""});

        // this.fetchServices();
        // this.setServices();
        // this.setServicesNavigation();

        console.log("mounted: services", this.services);
        console.log("mounted: services_navigation", this.services_navigation);
        console.log("mounted: services_all", this.services_all);
    },

    computed: {
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

            // console.log(this.$el);
            this.$forceUpdate();
        },

        addService(e) {
            e.preventDefault();

            console.log('addService()');

            const index = e.target.getAttribute('data-index');
            // this.services_added.push({'test': '11111'});
            // this.services_added.push(Vue.util.extend({}, this.apartment));
            // this.services_added.push(Vue.util.extend({}, {'test': index, 'test2': '2222'}));
            this.services_added.push(Vue.util.extend({}, this.service_to_add));

            console.log(this.services_added);

            // this.$forceUpdate();
        },

        removeService(index) {
            console.log('removeService()', index);
            // delete this.services_added[index];
            // this.$forceUpdate();
            Vue.delete(this.services_added, index);
            console.log(this.services_added);
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