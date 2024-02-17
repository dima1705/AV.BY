import React from "react";

const SelectBrand = ({options, defaultValue, value, onChange}) => {
    

    return(
        <div>
            <select 
                value={value}
                onChange={event => onChange(event.target.value)}
                >
                <option value="">{defaultValue}</option>
                {options.map(brand => 
                    <option key={brand.value} value={brand.value}>
                        {brand.brand}
                        </option>
                    )}
            </select>
        </div>
    )
}

export default SelectBrand