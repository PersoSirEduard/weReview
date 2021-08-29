import Feauture from "./Feauture"

const Landing = () => {
    return (
        <div className="landingContainer">
            <div className="mainInfo">
            <h1>
                Brain Canada
            </h1>
            <p>
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. Totam quaerat quo assumenda error ducimus aperiam quia hic molestiae, minima rem quam dolor accusantium consequuntur, tempore quae aut. Veritatis, labore modi?
            </p>
            <button>Submit your proposal</button>
            </div>
            <div className="mainFeatures">
                <Feauture featureName="Quick Apply" featureDescription="Apply in a few minutes, and get your proposal matched ASAP!" />
                <Feauture featureName="Quick Apply" featureDescription="Apply in a few minutes, and get your proposal matched ASAP!" />
                <Feauture featureName="Quick Apply" featureDescription="Apply in a few minutes, and get your proposal matched ASAP!" /> 
            </div>
        </div>
    )
}

export default Landing
