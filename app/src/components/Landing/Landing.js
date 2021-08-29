import SignIn from "./SignIn"
import { useState } from "react"
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import Application from "../Application/Application";

const Landing = () => {
    const [admin, showAdmin] = useState(false)

    let onclick = () => {
        showAdmin(!admin);
        console.log("clicked");
    }
    return (
        <Router>
            <Switch>
                <Route path="/" exact render={() => {
                    return (
                        <div className="landingContainer">
                            <div className="mainInfo">
                                <img src="app\public\background.png" alt="landing page illustration" className="landingPageImage"></img>
                                <p className="landingPageTxt">
                                    Get instant assessment reviews from Top Professionals with your next Nobel Prize Worthy Research.
                                </p>
                            </div>

                            <div className="buttons">
                                <Link to="/apply">
                                    <button className="button applyButton">Apply Now</button>
                                </Link>
                                <div className="adminSignIn">
                                    <button onClick={onclick} className="button adminButton">Access Admin</button>
                                    {admin ? <SignIn /> : console.log("Hello")}
                                </div>
                            </div>
                        </div>
                    );
                }} />
                <Route path="/apply" exact component={Application} />
            </Switch>
        </Router>
    )
}

export default Landing
