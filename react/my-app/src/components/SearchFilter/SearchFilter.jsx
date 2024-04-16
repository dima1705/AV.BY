import axios from "axios";
import React, { useEffect, useState, useMemo, lazy, Suspense, } from "react";
// import SelectBrand from "./MySelect/SelectBrand";
// import SelectModel from "./MySelect/SelectModel";
import { Link, useParams, useSearchParams } from "react-router-dom";
// import Auto from "../UsedAuto/Auto/Auto";
import { Select } from "antd";

import './SearchFilter.css'


const Auto = lazy(() => import('../UsedAuto/Auto/Auto'))

const SearchFilter = ({ brand }) => {



    const [auto, setAuto] = useState([])
    const [currentPage, setCurrentPage] = useState(1)
    const [fetching, setFetching] = useState(true)
    const limit = 10
    const [totalCount, setTotalCount] = useState(0)

    const [searchParams, setSearchParams] = useSearchParams()

    const brandQuery = searchParams.get('brand') || ''  // Получаем параметр запроса
    const modelQuery = searchParams.get('model') || ''
    const genQuery = searchParams.get('gen') || ''

    const yearQueryFrom = searchParams.get('year_from') || ''
    const yearQueryTo = searchParams.get('year_to') || ''

    const priceQueryFrom = searchParams.get('price_from') || ''
    const priceQueryTo = searchParams.get('price_to') || ''

    const volumeQueryFrom = searchParams.get('volume_from') || ''
    const volumeQueryTo = searchParams.get('volume_to') || ''

    const { Option } = Select;
    const [selectedBrand, setSelectedBrand] = useState(null)
    const [brands, setBrands] = useState([])
    const [selectedModel, setSelectedModel] = useState(null)
    const [models, setModels] = useState([])
    const [selectedGen, setSelectedGen] = useState(null)
    const [gen, setGen] = useState([])




    const handleSubmit = (e) => {
        e.preventDefault()
        const form = e.target

        const brand = selectedBrand
        const model = selectedModel
        const gen = selectedGen

        const year_from = form.year_from.value
        const year_to = form.year_to.value

        const price_from = form.price_from.value
        const price_to = form.price_to.value

        const volume_from = form.volume_from.value
        const volume_to = form.volume_to.value


        const params = {}

        if (brand.length) params.auto = brand
        if (model.length) params.model = model
        if (gen.length) params.gen = gen

        if (year_from.length) params.year_from = year_from
        if (year_to.length) params.year_to = year_to

        if (price_from.length) params.price_from = price_from
        if (price_to.length) params.price_to = price_to

        if (volume_from.length) params.volume_from = volume_from
        if (volume_to.length) params.volume_to = volume_to


        setSearchParams(params)

    }

    useEffect(() => {
        const getAuto = async () => {
            const response = await axios.get('http://127.0.0.1:8000/auto/all')
            setAuto(response.data)
        }
        getAuto()

        const getBrand = async () => {
            const response = await axios.get('http://127.0.0.1:8000/bmg/get_bmg')
            setBrands(response.data)
        }
        getBrand()

    }, [])

    const fetchModelsByBrand = (brandId) => {
        const selectedBrand = brands.find((brand) => brand.brand === brandId);
        if (selectedBrand) {
            setModels(selectedBrand.auto_model);

        }
        setSelectedModel(null);
    };
    // debugger
    const fetchGensByModel = (modelId) => {
        const selectedModel = models.find((model) => model.model === modelId);
        if (selectedModel) {
            setGen(selectedModel.auto_generation);

        }
        setSelectedGen(null);
    };


    return (
        <div>
            <div className="filter-title">
                Поиск по параметрам
            </div>
            <div className="filter">
                <form onSubmit={handleSubmit} >
                    <div className="main-filter">
                        <Select
                            showSearch
                            className="filter-select"
                            placeholder="Марка"
                            name="brand"
                            value={selectedBrand}
                            onChange={(value) => {
                                fetchModelsByBrand(value);
                                setSelectedBrand(value);
                            }}
                        >
                            {brands.map((brand) => (
                                <Option key={brand.id} value={brand.brand}>
                                    {brand.brand}
                                </Option>
                            ))}
                        </Select>


                        <Select
                            showSearch
                            className="filter-select"
                            placeholder="Модель"
                            name="model"
                            value={selectedModel }
                            onChange={(value) => {
                                fetchGensByModel(value);
                                setSelectedModel(value)
                            }}
                            disabled={!selectedBrand}
                        >
                            {models.map((model) => (
                                <Option key={model.id} value={model.model}>
                                    {model.model}
                                </Option>
                            ))}
                        </Select>
                        <Select
                            className="filter-select"
                            placeholder="Поколение"
                            name="gen"
                            value={selectedGen}
                            onChange={(value) => setSelectedGen(value)}
                            disabled={!selectedModel}
                        >
                            {gen.map((gen) => (
                                <Option key={gen.id} value={gen.generation}>
                                    {gen.generation}
                                </Option>
                            ))}
                        </Select>
                    </div>

                    <div className="add-filter">
                        <div className="year-filter">
                            <input type="searh" name="year_from" placeholder="Год от" />
                            <input type="searh" name="year_to" placeholder="до" />
                        </div>

                        <div className="price-filter">
                            <input type="searh" name="price_from" placeholder="Цена от" />
                            <input type="searh" name="price_to" placeholder="до" />
                        </div>

                        <div className="volume-filter">
                            <input type="searh" name="volume_from" placeholder="Объем от" />
                            <input type="searh" name="volume_to" placeholder="до" />
                        </div>
                    </div>




                    <div className="filter-button">
                        <input type="submit" value="Показать объявления" />
                    </div>

                </form>
            </div>

            <div className="auto-items">
                <div className="auto-count">
                    Найдено {auto.length} Объявлений
                </div>
                {auto.filter(auto => (
                    (auto.brand === brandQuery || brandQuery === '') &&
                    (auto.model === modelQuery || modelQuery === '') &&
                    (auto.generation_with_years === genQuery || genQuery === '') &&

                    (yearQueryFrom === '' || Number(auto.year) >= Number(yearQueryFrom)) &&
                    (yearQueryTo === '' || Number(auto.year) <= Number(yearQueryTo)) &&

                    (priceQueryFrom === '' || Number(auto.price_amount_usd) >= Number(priceQueryFrom)) &&
                    (priceQueryTo === '' || Number(auto.price_amount_usd) <= Number(priceQueryTo)) &&

                    (volumeQueryFrom === '' || Number(auto.engine_capacity) >= Number(volumeQueryFrom)) &&
                    (volumeQueryTo === '' || Number(auto.engine_capacity.replace(/л/, '').replace(/\s/, '')) <= Number(volumeQueryTo))
                )).map((car) => (
                    <Suspense fallback={<p>Loading...</p>} key={car.id}>
                        <Auto auto={car} key={car.id} />
                    </Suspense>
                ))
                }
            </div>
        </div >
    )
}

export default SearchFilter