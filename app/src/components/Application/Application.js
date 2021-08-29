import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import Success from "./Success";
const Input = ({ label, placeholder, className }) => {
    return (
        <div className={className}>
            <label>{label}</label>
            <input type="text" name={label} placeholder={placeholder} />
        </div>
    )
}

const Application = () => {
    return (

        <Router>
            <Switch>
                <Route path="/apply" exact render={() => {
                    return (
                        <div>
            <div className="applyTextContainer">
                <p className="applyHeader">Applicant Form</p>
                <p className="applyText">Hey there! We'd love to get to know you first before we redirect you with our recommended <span className="yellowHighlight">Research and Industry Professionals</span></p>
            </div>
            <form className="applicantForm">
                <Input label="Full Name" placeholder="Eg. Cody Coleman" className="nameInput" />
                <div className="applySectionOne">
                    <Input label="College Degree" placeholder="Eg. Biological Science" className="degreeInput" />
                    <Input label="Institution" placeholder="Eg. University of Alberta" className="collegeInput" />
                </div>
                <div className="applySectionTwo">
                    <Input label="Project Title" placeholder="Eg. Cognitive Neuroscience and Dementia" className="titleInput" />
                    <Input label="Project Link" placeholder="" className="linkInput" />
                </div>
                <div className="researchType">
                    <div className="pResearchTypeSelect">
                        <label>Primary Type of Research</label>
                        <select>

                        </select>
                    </div>
                    <div className="sResearchTypeSelect">
                        <label>Secondary Type of Research</label>
                        <select>

                        </select>
                    </div>

                </div>
                <div className="researchArea">
                    <div className="pResearchAreaSelect">
                        <label>Primary Research Area</label>
                        <select>

                        </select>
                    </div>
                    <div className="sResearchAreaSelect">
                        <label>Secondary Research Area</label>
                        <select>

                        </select>
                    </div>


                </div>
                <div className="formButtons">
                <button type="reset" className="resetButton">Reset</button>
                <Link to="/applied">
                <button type="submit" className="submitButton">Submit</button>
                </Link>
                </div>
            </form>
        </div>
                    );
                }}/>
                <Route path="/applied" exact component={Success} />
            </Switch>
        </Router>
    )
}

export default Application;
