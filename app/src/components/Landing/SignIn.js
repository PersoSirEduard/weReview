import { useState } from 'react'

const SignIn = () => {
    const [password, setPassword] = useState("");

    let handleSubmit = (e) => {
        e.preventDefault();
    }

    return (
        <form onSubmit={e => {handleSubmit(e)}} className="passwordInputContainer" style={{"display":"block"}}>
            <input value={password} onChange={e => setPassword(e.target.value)}  type="password" name="password" id="passwordInput" />
        </form>
    )
}

export default SignIn
