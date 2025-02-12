import './find.css'
import React, { useState, useEffect, useRef } from "react";

const DropDown = ({data,findid,companyid}) => {
    const [ddtoggled, setddtoggled] = useState(false)
    const [selected, setselected]=useState(null)

    console.log("from dropdown", data)


    // const ddoptions = [
    //     {
    //         id: 1,
    //         label: "xyz",
    //         value: "xuyuxu"
    //     }, {
    //         id: 1,
    //         label: "abc",
    //         value: "xuyuxu"
    //     },
    // ];


    return (
        <div className='dropdown'>
            <button className='toggle' onClick={() => {
                setddtoggled(!ddtoggled);
            }}>
                <span>{selected ? selected.company_name : "Select Company"} </span>
                <span>{ddtoggled ? '-' : '+'}</span>
                </button>

            <div className={`ddtextoptions ${ddtoggled ? "visible" : ""}`}>
                {data.map((option, index) => {
                    return <button className='options' key={index} onClick={()=>
                    {setselected(option)
                        setddtoggled(false)
                        console.log("kitti",option.id)
                        findid(option.id)
                    }} value={option.id}>{option.company_name}</button>;
                })}
            </div>
        </div>
    );
};
export default DropDown;