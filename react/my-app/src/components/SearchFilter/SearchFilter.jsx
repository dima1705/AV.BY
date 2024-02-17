import axios from "axios";
import React, { useEffect, useState, useMemo, } from "react";
import SelectBrand from "./MySelect/SelectBrand";
import UsedAuto from "../../Used_Auto";
import SelectModel from "./MySelect/SelectModel";
import { useParams } from "react-router-dom";

const SearchFilter = ({ brand }) => {

    const [auto, setAuto] = useState([]);
    const [selectedSort, setSelectedSort] = useState('');
    const [models, setModels] = useState([])
    const { id } = useParams()


    useEffect(() => {

        const getAuto = async () => {
            const response = await axios.get('http://127.0.0.1:8000/used_cars/all/')
            setAuto(response.data)
        }

        const getModel = async (id) => {
            const response = await axios.get(`http://127.0.0.1:8000/used_cars/gen_by_model_id/{id}?model_id=${id}`)
            setModels(response.data)
        }

        if (id) {
            getModel(id)
        }
        getAuto();
    }, [id, brand])


    const filterAuto = useMemo(() => {
        console.log(selectedSort)
        // console.log(auto.name)
        return auto.filter(auto => auto.name.replace("-", ' ').toLowerCase().includes(selectedSort.replace("-", ' ').toLowerCase()))
    }, [selectedSort, auto])


    const sortAuto = (sort, brandId) => {
        setSelectedSort(sort);
        setModels(brandId);
    };



    return (
        <div>
            <SelectBrand
                value={selectedSort}
                onChange={(sort) => sortAuto(sort, brand.id)}
                defaultValue="Марка"
                options={brand}
            />
            {/* <SelectModel
                value={selectedSort}
                onChange={sortAuto}
                defaultValue="Модель"
                options={models.filter((model) => model.brand_id === brand.id)}
            /> */}

            <UsedAuto auto={filterAuto} />
        </div>
    )
}

export default SearchFilter