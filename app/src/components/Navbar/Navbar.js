import NavItem from "./NavItem"

const Navbar = () => {
    return ( 
    <div className="navbar">
        <NavItem item = "wR" className="navbarLogo" />
        <div className="links">
            <NavItem item="Home" className="navItem" link="#"/>
            <NavItem item="Research" className="navItem" link="#" />
            <NavItem item="About" className="navItem" link="#" />
        </div>
        </div>
    )
}

export default Navbar