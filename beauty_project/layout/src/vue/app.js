import Vue from 'vue';

Vue.component('search-component', require('./components/SearchComponent').default);

new Vue({
    el: '#app',
    // data: {
    //     message: '!!!!!!!!! Hello from Webpack'
    // }

    // data() {
    //     return {
    //         message: '!!!!!!!!! Hello from Webpack'
    //     }
    // },

    // components: {
    //     Datepicker,
    // }
});
