Vue.component('radar-chart', {
  extends: VueChartJs.Radar,
  mounted () {
    this.renderChart({
      labels: ['清潔さ', '施設・設備', 'ロケーション', 'サービス', 'ラウンジ'],
      datasets: [
        {
          label:'評価',
          backgroundColor:'rgba(0, 200, 83, .5)',
          borderColor:"rgba(0, 200, 83, .8)",
          borderWidth:1,
          data: [90, 39, 60, 40, 39]
        }
      ]
    }, {responsive: true, maintainAspectRatio: false})
  }
})


var app = new Vue({
    el: '#app',
    delimiters: ['{$', '$}'],
    data: function data() {
        return {
            drawer:null,
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
            panel:[true,true]
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