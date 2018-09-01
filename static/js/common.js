var app = new Vue({
    el: '#app',
    data: function data() {
        return {
            drawer:null,
            items:['成田（NRT）', '羽田（ABC）', 'Fizz', 'Buzz'],
            countries:['アメリカ', '日本', '中国', 'フランス'],
            alliance:['スターアライアンス', 'ワンワールド', 'スカイチーム'],
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
            rating:3
        }
    },
    computed: {
        filterdData() {
			let options = this.options.opt_city
            return options.filter(o => o.dependency == this.support.home_province)
        }
    }
})