// function getAuto {
//     const API_URL = 'http://127.0.0.1:8000/used_cars/all/'

//     const axios.get(API_URL)
// }

import axios from 'axios'

export const CarsService = {
    async getAll() {
        const response = await axios.get('http://localhost:8000/used_cars/all/')

        return response.data
    },

    async getBrand() {
        const response = await axios.get('http://127.0.0.1:8000/used_cars/brand/all/')

        return response.data
    },


    async getById(id) {
        const response = await axios.get(`http://localhost:8000/used_cars/{id}?car_id=${id}`)

        return response.data
    },

    async create(data) {
        return axios.post('http://localhost:8000/used_cars/', data)
    },

    async getMainCategory() {
        const response = await axios.get('http://localhost:8000/used_cars/main_category/all/')

        return response.data
    }


}