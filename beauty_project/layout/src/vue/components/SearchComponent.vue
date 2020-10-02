<template>
    <form id="search-form" class="mt-3">
        <nav id="search-form__services-nav" class="mb-3">
            <a v-for="(item, index) in services"
                :key="item.id"
                :data-index="index"
                @click="getServiceGroupData"
                href="">{{ item.name }}</a>

            <!-- <a class="active" href="">Ногтевой сервис</a>
            <a href="">Парикмахерский зал</a>
            <a href="">Удаление волос</a>
            <a href="">Брови и ресницы</a>
            <a href="">Барбершоп</a> -->
        </nav>

        <div id="search-form__tiles">
            <div class="search-tiles-group">
                <div class="search-tile st-1">
                    <label for="">Местоположение или салон</label>
                    <select name="" id="search-tile-input__place" class="search-tile-input search-tile-input__place">
                        <option v-for="item in cities"
                            :key="item.id"
                            :value="item.id">{{ item.name }}</option>
                    </select>
                </div>
                <div class="search-tile st-2">
                    <label for="">Дата визита</label>
                    <input type="date" name="" id="search-tile-input__date" class="search-tile-input search-tile-input__date">
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

                <div class="search-tile st-4">
                    <label for="">Выберите услугу</label>
                    <select name="" id="search-tile-input__services" class="search-tile-input search-tile-input__services">
                        <option v-for="item in services_all"
                            :key="item.id"
                            :value="item.id">{{ item.name }}</option>
                    </select>
                </div>
                <div class="search-tile st-5">
                    <div class="search-tile__add-service">
                        <div class="search-tile__add-service-plus">+</div>
                        <div class="search-tile__add-service-text">добавить еще услугу из другой категории?</div>
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
export default {
    data() {
        return {
            api_services_url: '/api/services/',
            api_cities_url: '/api/cities/',
            services: [],
            services_all: [],
            cities: [],
        }
    },

    mounted() {
        this.fetchServices();
        this.fetchCities();
    },

    methods: {
        fetchServices() {
            fetch(this.api_services_url)
                .then(data => data.json())
                .then(this.setServices)
        },
        setServices(data) {
            this.services = data;
            this.services_all = data;
        },
        getServiceGroupData(e) {
            e.preventDefault();

            const index = e.target.getAttribute('data-index');
            this.services_all = this.services[index]['services'];

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
    },
}
</script>

<style lang="scss" scoped>
// h2 {
//     color: greenyellow;
// }
</style>