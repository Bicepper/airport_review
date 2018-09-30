var app = new Vue({
    el: '#app',
    delimiters: ['{$', '$}'],
    data: function data() {
        return {
            drawer:null,
            adminmenu:null,
            airports:[],
            countries:[],
            alliance:[],
            airlines:[],
            airportsselected:[],
            countryselected:[],
            allianceselected:[],
            sortitems:[],
            rating:3,
            agreement: false,
            dialogprivacy: false,
            dialogterms: false,
            rules: {
                required: function required(v) {return !!v || 'チェックが必要です';}
            },
            panel:[true,true],
            detailsortselect:{name:'新しい投稿順', abbr:0},
            detailsortlist:[
                {name:'新しい投稿順', abbr:0},
                {name:'参考になった順', abbr:1},
                {name:'評価が高い順', abbr:2},
                {name:'評価が低い順', abbr:3}
            ],
            detailcheckimage:false,
            usermenu:[
                {
                    action: 'restaurant',
                    active: true,
                    items:[
                        {title:'test'}
                    ]
                }
            ]
        }
    },
    computed: {
        filterAirport: {
            get: function(x) {
                return this.airportsselected;
            },
            set: function(y){
                this.airportsselected = y;
            }
        },
        filterCountry: {
            get: function(x) {
                return this.countryselected;
            },
            set: function(y){
                this.countryselected = y;
            }
        },
        filteredData() {
                // let options = this.airports;
                // console.log(options);
                // if (typeof(this.airlinesselected) !== 'number'){
                //     return options;
                // }else{
                //     //optionsで全て見て回る（pythonのmapみたいな感じ）
                //     return options.filter(o => o.id === this.airlinesselected)
                // }

                // let self = this.airports;
                // console.log(self);
                // let options = this.airports;
            if (this.airportsselected.length === 0 && this.countryselected.length === 0 && this.allianceselected.length === 0) {
                return this.airports;
            } else {
                var self = this;
                return self.airports
                    .filter(function(post){
                        if (self.airportsselected.length !== 0){
                            return post.id === self.airportsselected;
                        }else{
                            return self.airports;
                        }
                    })
                    .filter(function(post){
                        if (self.countryselected.length !== 0){
                            return post.country_id === self.countryselected;
                        }else{
                            return self.airports;
                        }
                    })
            }
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

        axios.get('/api/1.0/airlines/').then(function(response){
            for(var i=0; i < response.data.length; i++){
                self.airlines.push(response.data[i]);
            }
        });

        axios.get('/api/1.0/airports/').then(function(response){
            for(var i=0; i < response.data.length; i++){
                self.airports.push(response.data[i]);
            }
        });
    },
    methods: {
        clear: function() {
            this.airportsselected = '';
            this.countryselected = '';
        },
        remove (item) {
            const index = this.alliance.indexOf(item.name);
            if (index >= 0) this.alliance.splice(index, 1);
        }
    }
})