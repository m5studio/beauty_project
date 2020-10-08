<template>
    <form id="search-form" class="mt-3">
        <nav id="search-form__services-nav" class="mb-3">
            <a v-for="(item, index) in services"
                :key="item.id"
                :data-index="index"
                @click="getServiceGroupData"
                href="">{{ item.name }}</a>
        </nav>

        <div id="search-form__tiles">
            <div class="search-tiles-group">
                <div class="search-tiles-group__place-date-time">
                    <div class="search-tile st-1">
                        <label for="">Местоположение или салон</label>
                        <select name="" id="search-tile-input__place" class="search-tile-input search-tile-input__place">
                            <option>- Выберите город -</option>
                            <option v-for="item in cities"
                                :key="item.id"
                                :value="item.id">{{ item.name }}</option>
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
                    <div class="toClone">
                        <div class="search-tiles-group__add-service-wrap">
                            <div class="search-tile st-4">
                                <label for="">Выберите услугу</label>
                                <select name=""
                                    id="search-tile-input__services"
                                    class="search-tile-input search-tile-input__services">
                                    <option>- Выберите услугу -</option>
                                    <option v-for="item in services_all"
                                        :key="item.id"
                                        :value="item.id">{{ item.name }}</option>
                                </select>
                            </div>
                            <div class="search-tile st-5" @click="cloneItem">
                                <div class="search-tile__add-service">
                                    <div class="search-tile__add-service-plus">+</div>
                                    <div class="search-tile__add-service-text">добавить еще услугу из другой категории?</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="toClone" v-for="item in clonedServices" :key="item.id">
                        <div class="search-tiles-group__add-service-wrap">
                            <div class="search-tile st-4">
                                <label for="">Выберите услугу</label>
                                <select name=""
                                    id="search-tile-input__services"
                                    class="search-tile-input search-tile-input__services">
                                    <option>- Выберите услугу -</option>
                                    <option v-for="item in services_current"
                                        :key="item.id"
                                        :value="item.id">{{ item.name }}</option>
                                </select>
                                <div class="mt-3 text-right text-danger"
                                    @click="removeItem(item)"
                                    style="cursor: pointer;">X remove</div>
                            </div>
                            <div class="search-tile st-5" @click="cloneItem">
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
import Datepicker from 'vuejs-datepicker';
import * as lang from "vuejs-datepicker/src/locale";


export default {
    data() {
        return {
            // vuejs-datepicker language, initial date
            language: "ru",
            languages: lang,
            today: new Date(),

            api_services_url: '/api/services/',
            api_cities_url: '/api/cities/',

            services: [],
            services_all: [],
            services_current: [],

            clonedServices: [],

            cities: [],
        }
    },

    components: {
        Datepicker,
    },

    mounted() {
        this.fetchServices();
        this.fetchCities();
    },

    computed: {
    },

    methods: {
        fetchServices() {
            fetch(this.api_services_url)
                .then(data => data.json())
                .then(this.setServices)
        },
        setServices(data) {
            this.services = data;

            // fill services_all
            for (let i = 0; i < data.length; i++) {
                data[i]['services'].forEach(el => {
                    this.services_all.push(el);
                });
            }

            this.services_current = this.services_all;

            // Sort alphabetically
            // this.services_all.sort((a, b) => (a.name > b.name) ? 1 : -1)

            // console.log(this.services_all);
        },
        getServiceGroupData(e) {
            e.preventDefault();

            const index = e.target.getAttribute('data-index');
            // this.services_all = this.services[index]['services'];

            this.services_current = this.services[index]['services'];

            // Sort alphabetically
            // this.services_all.sort((a, b) => (a.name > b.name) ? 1 : -1)

            // console.log(this.services);
            // console.log(this.services_all);
        },
        fetchCities() {
            fetch(this.api_cities_url)
                .then(data => data.json())
                .then(this.setCities)
        },
        setCities(data) {
            this.cities = data;
        },

        cloneItem(e) {
            const toCloneDiv = e.target.closest(".toClone");
            const clone = toCloneDiv.cloneNode(true);
            this.clonedServices.push(clone);

            // console.log(clonedServices);

            // const index = e.target.getAttribute('data-index');
            // this.services_current = this.services[index]['services'];
        },
        removeItem(item) {
            this.clonedServices.splice(this.clonedServices.findIndex(w => w === item), 1);

            // console.log(this.clonedServices);

            // const item_index = this.clonedServices.indexOf(item);
            // this.clonedServices.splice(this.clonedServices[item_index], 1);
            // console.log(item_index);
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