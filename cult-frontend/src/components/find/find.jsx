import './find.css'
import React, { useState, useEffect, useRef } from "react";
import { IoMdArrowDropdown, IoMdArrowDropup } from "react-icons/io";

const DropDown = ({data,findid,companyid}) => {
    const [ddtoggled, setddtoggled] = useState(false)
    const [selected, setselected]=useState(null)


    return (
        <div className='dropdown'>
            <button className='toggle' onClick={() => {
                setddtoggled(!ddtoggled);
            }}>
                <span>{selected ? selected.company_name : "Select Company"} </span>
                <span>{ddtoggled ? <IoMdArrowDropup /> : <IoMdArrowDropdown />}</span>
                </button>

            <div className={`ddtextoptions ${ddtoggled ? "visible" : ""}`}>
                {data.map((option, index) => {
                    return <button className='options' key={index} onClick={()=>
                    {setselected(option)
                        setddtoggled(false)
                        findid(option.id)
                    }} value={option.id}>{option.company_name}</button>;
                })}
            </div>
        </div>
    );
};
export default DropDown;