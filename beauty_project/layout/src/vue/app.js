import Vue from 'vue';
import VueCloneya from 'vue-cloneya';


Vue.use(VueCloneya);

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
});