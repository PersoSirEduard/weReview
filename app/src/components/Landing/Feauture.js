const Feauture = ({featureName, featureDescription}) => {
    return (
        <div classNmae="card">
            <h2>
                {featureName}
            </h2>
            <p>
                {featureDescription}
            </p>
        </div>
    )
}

export default Feauture
