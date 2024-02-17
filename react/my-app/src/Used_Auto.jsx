import React from "react";
import Auto from "./Auto";

const UsedAuto = ({ auto }) => {

    return (
        <div>
            <table className="table">
                {/* <thead>
                    <tr>
                        <th scope="colName">Марка</th>
                        <th scope="colPrice_By">Цена в BYN</th>
                        <th scope="colPrice_Usd">Цена в USD</th>
                        <th scope="colYear">Год</th>
                        <th scope="colKpp">Коробка передач</th>
                        <th scope="colVolume">Объем</th>
                    </tr>
                </thead> */}
                <tbody>
                    {auto.map(auto => <Auto auto = {auto} key={auto.id}/>)}
                </tbody>
            </table>
        </div>
    )
}

export default UsedAuto