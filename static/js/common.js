var app = new Vue({
    el: '#app',
    delimiters: ['{$', '$}'],
    data: function data() {
        return {
            drawer:null,
            airports:[],
            countryselected:[],
            countries:[],
            alliance:[],
            airlinesselected:[],
            airlines:[],
            sortitems:[],
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
        filteredData() {
                let options = this.airports;
                if (typeof(this.airlinesselected) !== 'number'){
                    return options;
                }else{
                    //optionsで全て見て回る（pythonのmapみたいな感じ）
                    return options.filter(o => o.id === this.airlinesselected)
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
            this.airlinesselected = '';
            this.countryselected = '';
        }
    }
})