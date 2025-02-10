import './navbar.css'
const Navbar = () => {
    return (
        <div class='box'>
            <ul>
                {/* useref */}
                <li><a href="#home">HOME</a></li>
                <li><a href="#find">FIND</a></li>
                <li><a href="#about">ABOUT</a></li>
            </ul>
        </div>
    )
}
export default Navbar