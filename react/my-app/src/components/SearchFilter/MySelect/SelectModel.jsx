import React, { useState, useEffect } from "react";



const SelectModel = ({ value, onChange, options, defaultValue }) => {

    return (
        <div>
            <select
                value={value}
                onChange={event => onChange(event.target.value)}
            >
                <option value="">{defaultValue}</option>
                {options.map(model =>
                    <option key={model.id} value={model.value}>
                        {model.model}
                    </option>
                )}
            </select>
        </div>
    )
}

export default SelectModel