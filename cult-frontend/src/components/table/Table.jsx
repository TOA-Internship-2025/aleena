import React from 'react'
import './Table.css'

const Table = () => {
  return (
    <div className='table'>
        <table className='tabledata'>
            <tr>
                <th>Name</th>
                <th>Company ID</th> 
                <th>Cultivator Lot</th>
                <th>Crop Type</th>
            </tr>
            <tr>
                <td>Sandra</td>
                <td>W001</td>
                <td>L1</td>
                <td>Wheat</td>
            </tr>
            <tr>
                <td>Anna</td>
                <td>K056</td>
                <td>L7</td>
                <td>Rice</td>
            </tr>
        </table>


    </div>
  )
}

export default Table