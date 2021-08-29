const NavItem = ({item, className, link}) => {
    return (
        <a href={link} className={className}>
            {item}
        </a>
    )
}

export default NavItem
