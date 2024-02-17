import React from "react";

import axios from "axios"
import { useState, useEffect } from "react";


import CatalogBrands from "../../components/CatalogBrand/CatalogBrands";
import UsedAuto from "../../Used_Auto";
import Pagination from "../../services/Pagination";

import './Transport.css'
import SearchFilter from "../../components/SearchFilter/SearchFilter.jsx";

const API_URL = 'http://127.0.0.1:8000/used_cars/all/'
const API_URL_BRAND = 'http://127.0.0.1:8000/used_cars/brand/all/'

export const Transport = () => {

   
    const [currentPage, setCurrentPage] = useState(1)
    const [carsPerPage] = useState(15)
    const [brand, setBrand] = useState([])

    useEffect(() => {
        

        const getBrand = async () => {
            const response = await axios.get(API_URL_BRAND)
            setBrand(response.data)
        }

        // getAuto()
        getBrand()
    }, [])


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
                    <CatalogBrands brand={brand}/>
                    <SearchFilter brand={brand}/>
                    {/* <UsedAuto auto={currentAuto} /> */}
                    {/* <Pagination
                        carsPerPage={carsPerPage}
                        totalCars={auto.length}
                        paginate={paginate}
                    /> */}
                </div>
            </div>
            <div className="add-container">
                <div className="news">
                    <h1 className="news-title">
                        Автожурнал
                    </h1>
                    <div className="news-items">
                        <div className="news-item">
                        Белорусы открыли СТО в Испании, однако власти бизнес закрыли. Почему?
                            <div className="news-meta">
                                <span className="news-category">Авторынок</span>
                                <span className="news-date">3 часа назад</span>
                            </div>
                        </div>
                        <div className="news-item">
                            Mazda показала новый кроссовер CX-70
                            <div className="news-meta">
                                <span className="news-category">Авторынок</span>
                                <span className="news-date">3 часа назад</span>
                            </div>
                        </div>
                        <div className="news-item">
                        Новинки от BELGEE, и что будет с утильсбором в Беларуси. Подводим итоги большой пресс-конференции БАА
                            <div className="news-meta">
                                <span className="news-category">Авторынок</span>
                                <span className="news-date">3 часа назад</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    )
}

