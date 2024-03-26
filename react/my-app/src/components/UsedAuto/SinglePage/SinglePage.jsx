import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from 'axios'
import AutoJurnal from "../../AutoJournal/Autojurnal";

import './SinglePage.css'


export const SinglePage = () => {

    const { id } = useParams()
    const [auto, setAuto] = useState([])
    const [photos, setPhotos] = useState([])

    useEffect(() => {
        const getAutoById = async () => {
            const response = await axios.get(`http://127.0.0.1:8000/auto/${id}`)
            setAuto(response.data)
        }

        getAutoById()

        const getPhoto = async () => {
            const response = await axios.get(`http://127.0.0.1:8000/photos/${id}`)
            setPhotos(response.data[0])
            }  
        

        getPhoto()
    
    }, [id])
    console.log(photos)

    return (
        <div className="auto-item">

            <div className="auto-card">
                {auto.map(auto => (
                    <div className="auto-card-item">
                        <div className="auto-card-name">
                            <div className="auto-card-title">
                                <h1>{auto.brand}&nbsp;{auto.model}&nbsp;{auto.generation_with_years.split(' ')[0]},&nbsp;{auto.year}г.&nbsp;в г.&nbsp;{auto.location.split(',')[0]}</h1>
                            </div>
                            <div className="auto-card-date">
                                Опубликовано вчера 
                            </div>
                        </div>
                        <div className="auto-card-info">
                               <div 
                                key={photos.id} 
                                className="auto-card-photo"
                                style={{backgroundImage: `url(${photos})`}}
                                /> 
                            <div className="auto-card-params">
                                <div  className="param-price-byn">
                                    {auto.price_amount_byn} р.
                                </div>
                                <div className="param-price-usd">
                                    ≈ {auto.price_amount_usd} $
                                </div>
                                <div className="param-info">
                                    {auto.year},&nbsp;
                                    {auto.transmission_type},&nbsp;{auto.engine_capacity},&nbsp;{auto.engine_type},

                                </div>
                                <div className="param-probeg">
                                    {auto.mileage_km} км
                                </div>
                                <div className="param-dop-info">
                                    {auto.body_type},&nbsp;
                                    {auto.drive_type},&nbsp;
                                    {auto.color}
                                </div>
                                <div className="param-power">
                                    {auto.power} л.с.,&nbsp;расход {auto.fuel_consumption} л.
                                </div>

                                <div className="param-buttons">
                                    <button className="dialogs">Написать продавцу</button> 
                                    <button className="phone">Показать телефон</button> 
                                </div>
                            </div>
                        </div>
                        <div className="auto-card-comment">
                            <h4>Описание</h4>
                            <p>{auto.description}</p>
                                {console.log(auto.power)}
                        </div>
                    </div>
                ))
                }
            </div>

            <div className="auto-jurnal">
                <AutoJurnal />
            </div>
        </div>
    )
}