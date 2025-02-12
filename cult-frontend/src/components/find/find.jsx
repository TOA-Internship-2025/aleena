import './find.css'
import React, { useState, useEffect, useRef } from "react";

const DropDown = () => {
    const [ddtoggled, setddtoggled] = useState(false)
    const [selected, setselected]=useState(null)
    // const ddRef = useRef(null)
    // useEffect{()=>{
    //     if (ddRef.current){
    //         console.log(ddRef.current)
    //     }
    // }}

    const ddoptions = [
        {
            id: 1,
            label: "xyz",
            value: "xuyuxu"
        }, {
            id: 1,
            label: "abc",
            value: "xuyuxu"
        },
    ];


    return (
        <div className='dropdown'>
            <button className='toggle' onClick={() => {
                setddtoggled(!ddtoggled);
            }}>
                <span>{selected ? selected.label : "Select Company"} </span>
                <span>{ddtoggled ? '-' : '+'}</span>
                </button>
            <div className={`ddtextoptions ${ddtoggled ? "visible" : ""}`}>
                {ddoptions.map((option, index) => {
                    return <button className='options' onClick={()=>
                    {setselected(option)
                        setddtoggled(false)
                    }}>{option.label}</button>;
                })}
            </div>
        </div>
    );
};
export default DropDown;