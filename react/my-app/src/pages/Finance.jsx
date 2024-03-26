import React, { useState, useEffect } from "react";
import axios from "axios";
import { Select } from "antd";

export const Finance = () => {

    const { Option } = Select;
    const [selectedBrand, setSelectedBrand] = useState(null)
    const [brands, setBrands] = useState([])
    const [selectedModel, setSelectedModel] = useState(null)
    const [models, setModels] = useState([])
    const [selectedGen, setSelectedGen] = useState(null)
    const [gen, setGen] = useState([])

    useEffect(() => {
        const getBrand = async () => {
            const response = await axios.get('http://127.0.0.1:8000/bmg/get_bmg')
            setBrands(response.data)
        }
        getBrand()
        console.log(brands)

    }, [])

    const fetchModelsByBrand = (brandId) => {
        const selectedBrand = brands.find((brand) => brand.id === brandId);
        if (selectedBrand) {
            setModels(selectedBrand.auto_model);
        }
        setSelectedModel(null);
    };
    // debugger
    const fetchGensByModel = (modelId) => {
        const selectedModel = models.find((model) => model.id === modelId);
        if (selectedModel) {
            setGen(selectedModel.auto_generation);
        }
        setSelectedGen(null);
    };

    return (
        <div>
            <Select
                // className="filter-select"
                placeholder="Марка"
                name="brand"
                value={selectedBrand}
                onChange={(value) => {
                    fetchModelsByBrand(value);
                    setSelectedBrand(value);
                  }}
            >
                {brands.map((brand) => (
                    <Option key={brand.id} value={brand.id}>
                        {brand.brand}
                    </Option>
                ))}
            </Select>
            <Select
                // className="filter-select"
                placeholder="Модель"
                name="model"
                value={selectedModel}
                onChange={(value) => {
                    fetchGensByModel(value);
                    setSelectedModel(value)
                    }}
                disabled={!selectedBrand}
            >
                {models.map((model) => (
                    <Option key={model.id} value={model.id}>
                        {model.model}
                    </Option>
                ))}
            </Select>
            <Select
                // className="filter-select"
                placeholder="Поколение"
                name="gen"
                value={selectedGen}
                onChange={(value) => setSelectedGen(value)}
                disabled={!selectedModel}
            >
                {gen.map((gen) => (
                    <Option key={gen.id} value={gen.id}>
                        {gen.generation}
                    </Option>
                ))}
            </Select>


        </div>
    )
}

