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
            lounges:[],
            reviews:[],
            airportsselected:[],
            countryselected:[],
            allianceselected:[],
            airlineselected:[],
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
            ],
            rate:{
                emptyIcon: 'far fa-star',
                fullIcon: 'fas fa-star',
                halfIncrements: false,
                hover: true,
                length: 5,
                rating: 3,
                text:'普通',
                readonly: false
            },
            reviewairport:null
        }
    },
    computed: {
        filterAirport: {
            get: function(x){
                return this.airportsselected;
            },
            set: function(y){
                this.airportsselected = y;
            }
        },
        filterCountry: {
            get: function(x){
                return this.countryselected;
            },
            set: function(y){
                this.countryselected = y;
            }
        },
        filterAirlines:{
            get: function(x){
                return this.airlineselected;
            },
            set: function(y){
                this.airlineselected = y;
            }
        },
        filterAlliance:{
            get: function(x){
                return this.allianceselected;
            },
            set: function(y){
                this.allianceselected = y;
            }
        },
        filteredData() {
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
        },
        filteredLoungeData() {
            if (this.airportsselected.length === 0 &&
                this.countryselected.length === 0 &&
                this.allianceselected.length === 0 &&
                this.airlineselected.length === 0){
                return this.lounges;
            } else {
                var self = this;
                return self.lounges
                    .filter(function(post){
                        if (self.airportsselected.length !== 0){
                            return post.airport.id === self.airportsselected;
                        }else{
                            return self.lounges;
                        }
                    })
                    .filter(function(post){
                        if (self.countryselected.length !== 0){
                            return post.airport.country_id === self.countryselected;
                        }else{
                            return self.lounges;
                        }
                    })
                    .filter(function(post){
                        if (self.airlineselected.length !== 0){
                            return post.airline.id === self.airlineselected;
                        }else{
                            return self.lounges;
                        }
                    })
                    .filter(function(post){
                        if (self.allianceselected.length !== 0){
                            return post.alliance.id === self.allianceselected;
                        }else{
                            return self.lounges;
                        }
                    })
            }
        },
        reviewid:{
            get: function(x) {
                return this.reviewairport;
            },
            set: function(uu){
                this.reviewairport = uu;
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

        axios.get('/api/1.0/lounges/').then(function(response){
            for(var i=0; i < response.data.length; i++){
                self.lounges.push(response.data[i]);
            }
        });

        axios.get('/api/1.0/reviews/').then(function(response){
           for(var i=0; i < response.data.length; i++){
               self.reviews.push(response.data[i]);
           }
        });

        //画面遷移したときのretainした値を取得
        var rating_val = Number($('#id_rate_synthesis').val());
        self.rate.rating = rating_val;
        if(rating_val === 1){
            self.rate.text = '最悪';
        }else if(rating_val === 2){
            self.rate.text = '悪い';
        }else if(rating_val === 3){
            self.rate.text = '普通';
        }else if(rating_val === 4){
            self.rate.text = '良い';
        }else if(rating_val === 5){
            self.rate.text = '最高';
        }else{
            self.rate.text = '評価なし';
        }
    },
    methods: {
        clear: function() {
            this.airportsselected = '';
            this.countryselected = '';
            this.airlineselected = '';
            this.allianceselected = '';
        },
        remove (item) {
            const index = this.alliance.indexOf(item.name);
            if (index >= 0) this.alliance.splice(index, 1);
        },
        slideselect: function(id){
            // console.log($(event.target));
            // console.log(event);
            // $('#' + id).val(this.rate[id]);
            $('#' + id).val(this.rate.rating);
            if(this.rate.rating === 1){
                this.rate.text = '最悪';
            }else if(this.rate.rating === 2){
                this.rate.text = '悪い';
            }else if(this.rate.rating === 3){
                this.rate.text = '普通';
            }else if(this.rate.rating === 4){
                this.rate.text = '良い';
            }else if(this.rate.rating === 5){
                this.rate.text = '最高';
            }else{
                this.rate.text = '評価なし';
            }
        }
    }
})