import React, { useEffect, useState } from "react";
import { CarsService } from "../services/services";
import axios from 'axios'
import Brand from "../components/CatalogBrand/Catalog";
import { Link, useSearchParams } from "react-router-dom";

export const Examples = () => {

    const [auto, setAuto] = useState([])
    const [searchParams, setSearchParams] = useSearchParams()

    const autoQuery = searchParams.get('auto') || ''  // Получаем параметр запроса
    const modelQuery = searchParams.get('model') || ''
    const genQuery = searchParams.get('gen') || ''

    const yearQueryFrom = searchParams.get('year_from') || ''
    const yearQueryTo = searchParams.get('year_to') || ''

    const priceQueryFrom = searchParams.get('price_from') || ''
    const priceQueryTo = searchParams.get('price_to') || ''

    const volumeQueryFrom = searchParams.get('volume_from') || ''
    const volumeQueryTo = searchParams.get('volume_to') || ''

    const handleSubmit = (e) => {
        e.preventDefault()
        const form = e.target

        const brand = form.brand.value
        const model = form.model.value
        const gen = form.gen.value

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
        const getAutoById = async () => {
            const response = await axios.get('http://localhost:8000/used_cars/all/')
            setAuto(response.data)

            // console.log(response.data)
        }

        getAutoById()
    }, [])



    return (
        <div>
            <form autoComplete="off" onSubmit={handleSubmit}>
                <div>
                    <input type="searh" name="brand" placeholder="Марка" />
                    <input type="searh" name="model" placeholder="Модель" />
                    <input type="searh" name="gen" placeholder="Поколение" />
                </div>

                <div>
                    <input type="searh" name="year_from" placeholder="Год от" />
                    <input type="searh" name="year_to" placeholder="до" />
                </div>

                <div>
                    <input type="searh" name="price_from" placeholder="Цена от" />
                    <input type="searh" name="price_to" placeholder="до" /> USD
                </div>

                <div>
                    <input type="searh" name="volume_from" placeholder="Объем от" />
                    <input type="searh" name="volume_to" placeholder="до" /> л.
                </div>



                <input type="submit" value="Search" />
            </form>

            {
                auto.filter(
                    car =>
                        (car.name.toLowerCase().includes(autoQuery.toLowerCase()) || autoQuery === '') &&
                        (car.name.toLowerCase().includes(modelQuery.toLowerCase()) || modelQuery === '') &&
                        (car.name.toLowerCase().includes(genQuery.toLowerCase()) || genQuery === '') &&

                        (yearQueryFrom === '' || Number(car.year.replace(/г./, '')) >= Number(yearQueryFrom)) &&
                        (yearQueryTo === '' || Number(car.year.replace(/г./, '')) <= Number(yearQueryTo)) &&

                        (priceQueryFrom === '' || Number(car.price_for_usd.replace(/≈/, '').replace(/\s/, '')) >= Number(priceQueryFrom)) &&
                        (priceQueryTo === '' || Number(car.price_for_usd.replace(/≈/, '').replace(/\s/, '')) <= Number(priceQueryTo)) &&

                        (volumeQueryFrom === '' || Number(car.volume.replace(/л/, '').replace(/\s/, '')) >= Number(volumeQueryFrom)) &&
                        (volumeQueryTo === '' || Number(car.volume.replace(/л/, '').replace(/\s/, '')) <= Number(volumeQueryTo))
                ).map(car => (
                    <Link key={car.id} to={`/${car.id}`}>
                        <li>{car.name}</li>{car.price_for_usd.replace(/≈/, '').replace(/\s/, '')}{car.year.replace(/г./, '')}{car.volume.replace(/л/, '').replace(/\s/, '')}
                    </Link>
                ))
            }
        </div>
    )
}

