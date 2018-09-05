var app = new Vue({
    el: '#app',
    delimiters: ['{$', '$}'],
    data: function data() {
        return {
            drawer:null,
            items:['成田（NRT）', '羽田（ABC）', 'Fizz', 'Buzz'],
            countries:[],
            alliance:[],
            airline:['全日空', 'ルフトハンザ', 'ブリティッシュエアウェイズ', '中国東方航空'],
            cards:[
                { title: 'Best airlines01', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines02', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines03', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines04', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines05', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines06', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines07', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines08', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines09', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines11', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines12', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines13', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 }
            ],
            rating:3,
            agreement: false,
            dialogprivacy: false,
            dialogterms: false,
            rules: {
                required: function required(v) {return !!v || 'チェックが必要です';}
            }
        }
    },
    computed: {
        filterdData() {
			let options = this.options.opt_city
            return options.filter(o => o.dependency == this.support.home_province)
        }
    },
    created: function() {
        var self = this;
        axios.get('/api/1.0/countries/').then(function(response){
            for(var i=0; i < response.data.length; i++){
                self.countries.push(response.data[i]);
            }
        });

        axios.get('/api/1.0/alliances/').then(function(response){
            for(var i=0; i < response.data.length; i++){
                self.alliance.push(response.data[i]);
            }
        });
    }
})