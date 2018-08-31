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
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 },
                { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 3, mdflex: 6 }
            ]
        }
    },
    computed: {
        filterdData() {
			let options = this.options.opt_city
            return options.filter(o => o.dependency == this.support.home_province)
        }
    }
})