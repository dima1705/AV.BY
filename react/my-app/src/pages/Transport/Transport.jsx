import React from "react";

import axios from "axios"
import { useState, useEffect } from "react";

import CatalogBrands from "../../components/CatalogBrand/CatalogBrands";
import Pagination from "../../services/Pagination";

import './Transport.css'
import SearchFilter from "../../components/SearchFilter/SearchFilter.jsx";

import { CarsService } from "../../services/services.js";
import AutoJurnal from "../../components/AutoJournal/Autojurnal.jsx";





const API_URL = 'http://127.0.0.1:8000/used_cars/all/'
const API_URL_BRAND = 'http://127.0.0.1:8000/av/brands'

export const Transport = () => {

   
    const [currentPage, setCurrentPage] = useState(1)
    const [carsPerPage] = useState(15)
    const [brand, setBrand] = useState([])

    useEffect(() => {
        

        const getBrand = async () => {
            const response = await axios.get('http://127.0.0.1:8000/av/brands')
            setBrand(response.data)
        }
        
        // getAuto()
        getBrand()
    }, [])

    // debugger
    // const lastAutoIndex = currentPage * carsPerPage
    // const firstAutoIndex = lastAutoIndex - carsPerPage
    // const currentAuto = auto.slice(firstAutoIndex, lastAutoIndex)


    const paginate = pageNumber => setCurrentPage(pageNumber)

    return (
        <div className="wrapper">
            <div className="container">
                <div className="main-container">
                    <div className="title">
                        <h1>Объявления о продаже автомобилей с пробегом в Беларуси</h1>
                    </div>
                    {/* <CatalogBrands brand={brand}/> */}
                    {brand.map(brand => <CatalogBrands brand={brand} key={brand.id} />)}
                    <SearchFilter/>
                    {/* <UsedAuto auto={currentAuto} /> */}
                    {/* <Pagination
                        carsPerPage={carsPerPage}
                        totalCars={auto.length}
                        paginate={paginate}
                    /> */}
                    
                </div> 
            </div> 
            <AutoJurnal/>  
        </div>

    )
}

