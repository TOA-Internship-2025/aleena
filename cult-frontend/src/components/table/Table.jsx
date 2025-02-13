import './Table.css'
import { useEffect, useState } from 'react'

const Table = ({tabledata}) => {
    console.log("ethio",tabledata)


const celldata=tabledata.map((item,key)=>{
        return (
            <tr>
                <td>{item.id}</td>
                <td>{item.cultivator_name}</td>
                <td>{item.cultivation_lot}</td>
                <td>{item.crop_type}</td>
            </tr>
        )
    })



console.log("celldatas??",celldata)

  return (
    
    <div className='table'>
        <table className='tabledata'>
            <tr>
            <th>Cultivator ID</th> 
                <th>Name</th>
                <th>Cultivator Lot</th>
                <th>Crop Type</th>
            </tr>
            {tabledata.length>0 ? celldata : 
            <tr><td colSpan={4} align='center'>Details Not Available
                </td></tr>}
        </table>

    </div>
  )
}

export default Table