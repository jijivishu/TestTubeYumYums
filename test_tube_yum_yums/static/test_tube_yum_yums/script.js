/*
 * This file deals with everything happening on the front-end of the website.

 * It is divided into following two sections:
 * The first section(till 768th line): Responsible for authenticating the user.
 * The second section(from 769th line): Responsible for accepting the blood test data from an authenticated user.
*/



// If user is unlogged, the login form is displayed
if (document.querySelector('#unlogged')) {
    ReactDOM.render(<Login />, document.querySelector('#unlogged'))
}


// The sole purpose of this function is to switch between Register Form and the Login Form 
function switchMenu(name) {
    if (name === "Register") {
        ReactDOM.render(<Login />, document.querySelector('#unlogged'))
    }
    else if (name === "Login") {
        ReactDOM.render(<Register />, document.querySelector('#unlogged'))
    }
}


/* 
For the first section, we render the login menu component and allow an option to switch it with register menu component.
The login form has an Email input field, a password input field and a submit button 
*/
function Login() {

    // Username and Password when submitted through form, are stored in the following state object
    const [loginInputs, updateLoginInputs] = React.useState({
        email: "",
        password: ""
    })

    // If Login Form has any error message, it is stored in this state object
    const [error, setError] = React.useState(null)

    // Login form fields are rendered dynamically through this array containing html input tag attributes for each field
    const loginInputFields = [
        {
            id: 1,
            name: "email",
            type: "email",
            placeholder: "johnharvard@harvard.edu",
            label: "Email address",
            errorMessage: "is not valid",
            required: true
        },
        {
            id: 2,
            name: "password",
            type: "password",
            placeholder: "********",
            label: "Password",
            errorMessage: "cannot be empty",
            required: true
        },
    ]

    // This function is called the moment an input field experiences a change and it's value is updated accordingly
    const updateFields = (e) => {
        updateLoginInputs({ ...loginInputs, [e.target.name]: e.target.value })
    }

    // This function is responsible for sending Login Data entered by the user to the server...
    // ...through the sendToServer('process_name', data to be sent to the server, setState function for error) function 
    const sendLoginData = (e) => {
        e.preventDefault()
        sendToServer("Login", loginInputs, setError)
    }

    // Form code (to distinguish between login and register), fields and state object and... 
    // ...callback functions for updation and submission are sent for rendering the form
    return (
        <FormWrap formCode="0" fields={loginInputFields} updation={updateFields} submission={sendLoginData} error={error} />
    )
}


/* 
Whenever the user clicks on the "Register here" link in the Login Form, this component containing the Register Form is rendered.
The register form is a three page form where only first page is compulsory to fill.

The first page contains input fields for First Name, Last Name, Email, Date of Birth and Password.

The second page asks users to select their Country and enter their weight and height
The weight and height can be entered in kg/lb and in/cm respectively.
The values are converted in kg and cm before sending them to the server.

The third page asks user about their Health Information (Most recent diabetes(AST) and Blood Pressure measurements)

Apart from that, page contains a skip(simply moves to next page) and a next(submits entered values) button.
On Page 3, all the buttons act as submit button.
*/
function Register() {

    // All the inputs, when submitted through form, are stored in the following state object
    const [registerInputs, updateRegisterInputs] = React.useState({
        firstName: "",
        lastName: "",
        email: "",
        dob: "",
        password: "",
        confirmation: "",
        country: "",
        wUnit: "kg",
        weight: "",
        hUnit: "in",
        height: "",
        bp: false,
        systolic: "",
        diastolic: "",
        diabetes: false,
        ast: ""
    })

    // Register form fields are rendered dynamically through this array of arrays.
    // Outer array has individual pages of registration form as child while inner array has... 
    // ...html input-tag attributes for each form field of a page.
    const registerInputFields = [
        [
            {
                id: 1,
                name: "firstName",
                type: "text",
                placeholder: "John",
                label: "First Name",
                errorMessage: "cannot be empty",
                required: true
            },
            {
                id: 2,
                name: "lastName",
                type: "text",
                placeholder: "Harvard",
                label: "Last Name",
                errorMessage: "cannot be empty",
                required: true
            },
            {
                id: 3,
                name: "email",
                type: "email",
                placeholder: "johnharvard@harvard.edu",
                errorMessage: "is invalid",
                label: "Email",
                required: true
            },
            {
                id: 4,
                name: "dob",
                type: "date",
                label: "Date of Birth",
                errorMessage: "cannot be empty",
                required: true
            },
            {
                id: 5,
                name: "password",
                type: "password",
                placeholder: "********",
                pattern: '(?!^\\d+$)^.{8,}',
                title: "Password must contain atleast 8 characters and must not be entirely numeric.",
                errorMessage: "must contain atleast 8 characters and must not be entirely numeric.",
                label: "Password",
                required: true
            },
            {
                id: 6,
                name: "confirmation",
                type: "password",
                placeholder: "********",
                pattern: registerInputs.password,
                title: "Passwords must match",
                label: "Re-enter Password",
                errorMessage: "not matching",
                required: true
            }
        ],
        [
            {
                id: 7,
                name: "country",
                type: "text",
                placeholder: "Select your country",
                label: "Country",
                errorMessage: "is required",
                required: true
            },
            {
                id: 8,
                name: "weight",
                type: "number",
                min: "0",
                step: "0.01",
                placeholder: "Enter your body weight",
                label: "Weight",
                errorMessage: "is required",
                required: true
            },
            {
                id: 9,
                name: "height",
                type: "number",
                min: "0",
                step: "0.01",
                placeholder: "Enter your height",
                label: "Height",
                errorMessage: "is required",
                required: true
            }
        ],
        [
            {
                id: 10,
                name: "bp",
                type: "checkbox",
                label: "Blood Pressure",
                errorMessage: "is required",
                required: true
            },
            {
                id: 11,
                name: "diabetes",
                type: "checkbox",
                label: "Diabetes",
                errorMessage: "is required",
                required: true
            },
            {
                id: 12,
                name: "systolic",
                type: "number",
                min: "0",
                step: "0.01",
                placeholder: "in mm of Hg",
                label: "Systolic",
                errorMessage: "is required",
                required: true
            },
            {
                id: 13,
                name: "diastolic",
                type: "number",
                min: "0",
                step: "0.01",
                placeholder: "in mm of Hg",
                label: "Diastolic",
                errorMessage: "is required",
                required: true
            },
            {
                id: 14,
                name: "ast",
                type: "number",
                min: "0",
                step: "0.01",
                placeholder: "in U/L",
                label: "AST value",
                errorMessage: "is required",
                required: true
            }
        ]
    ]

    // If Register Form has any error message, it is stored in this state object
    const [error, setError] = React.useState(null)

    // This function is called the moment an input field experiences a change and it's value is updated accordingly
    // Whenever a checkbox is unchecked, it's child input fields are resetted
    const updateRegisterFields = (e) => {
        if (e.target.type === "checkbox") {
            if (e.target.checked) updateRegisterInputs({ ...registerInputs, [e.target.name]: true })
            else {
                if (e.target.name === "diabetes") updateRegisterInputs({ ...registerInputs, [e.target.name]: false, ["ast"]: "" })
                else if (e.target.name === "bp") updateRegisterInputs({ ...registerInputs, [e.target.name]: false, ["systolic"]: "", ["diastolic"]: "" })
            }
        }
        else updateRegisterInputs({ ...registerInputs, [e.target.name]: e.target.value })
    }

    // Whenever the Skip button is clicked on a registration form-page, all the inputs on that page are omitted
    function skipPage(pageNum) {
        if (pageNum === 1) {
            updateRegisterInputs({ ...registerInputs, ["country"]: "", ["weight"]: "", ["height"]: "" })
        }
        else if (pageNum === 2) {
            updateRegisterInputs({ ...registerInputs, ["systolic"]: "", ["diastolic"]: "", ["ast"]: "", ["bp"]: false, ["diabetes"]: false })
        }
    }

    // This function is responsible for sending Register Data entered by the user to the server... 
    // ...through the sendToServer('process_name', data to be sent to the server, setState function for error) function, when... 
    // ...triggered on the last page of the registration form.
    function sendRegisterData(event, pageNum) {
        if (pageNum === registerInputFields.length - 1) {

            // Send data to server
            sendToServer("Register", registerInputs, setError);
        }
        event.preventDefault()
        return false
    }

    // Form code (to distinguish between login and register), fields, state objects and... 
    // ...appropriate callback functions(for skipping a page, updating a field and... 
    // ...submitting the registration form) are sent for rendering the form.
    return (
        <FormWrap formCode="1" fields={registerInputFields} updation={updateRegisterFields} submission={sendRegisterData} values={registerInputs} skip={skipPage} error={error} />
    )
}


// This component renders layout of the form and the child components containing input fields
function FormWrap(props) {
    return (
        <div class='h-screen flex justify-center items-center'>

            {props.formCode !== '0'
                ?
                <div class='w-4/5 sm:w-2/3 bg-white rounded-lg shadow-lg p-10 m-10'>
                    <RegisterForm fields={props.fields} updation={props.updation} submission={props.submission} values={props.values} skip={props.skip} error={props.error} />
                </div>
                :
                <div class='lg:w-2/5 md:w-1/2 w-4/5 bg-white rounded-lg shadow-lg p-10'>
                    <LoginForm fields={props.fields} updation={props.updation} submission={props.submission} error={props.error} />
                </div>
            }

        </div>
    )
}


// This component aligns form fields of Login Form and renders Input field component desired number of times as children. 
function LoginForm(props) {
    return (
        <form onSubmit={props.submission}>
            <h1 class="text-center text-2xl mb-2 text-gray-600 font-bold font-sans"> Log In </h1>
            {props.error ? <h3 class='text-center my-4 text-md text-red-800 font-medium font-serif'>{props.error}</h3> : ''}

            {/* Rendering every input field*/}
            {props.fields.map((input) => (
                <FormInput key={input.id} {...input} onChange={props.updation} />
            ))}



            <div class="flex justify-between items-end">
                <div>
                    Not a member?
                    <p onClick={(e) => { e.preventDefault(); switchMenu("Login") }} class="cursor-pointer hover:text-indigo-800  hover:font-semibold">  Register here</p>
                </div>
                <div class="w-1/2 sm:w-2/3 lg:w-1/3 ">
                    <Button placeholder="Login" type="submit" />
                </div>
            </div>
        </form>
    )
}


// This component aligns form fields of Register Form and renders Input field component... 
// ...desired number of times based on their type as children. 
// It is also responsible for displaying input fields as per their respective pages
function RegisterForm(props) {

    // Current page number (-1) of the form is stored in this state variable. Default: Page 1
    const [currentPage, setCurrentPage] = React.useState(0)

    // This function increments the page number unless it's the last page of the registration form.
    function nextPage() {
        setCurrentPage(() => {
            if (currentPage === props.fields.length - 1) return currentPage
            return currentPage + 1
        })
    }

    // This function decrements the page number unless it's the first page of the registration form.
    // NOTE: NO LONGER IN USE
    function prevPage() {
        setCurrentPage(() => {
            if (currentPage === 0) return currentPage
            return currentPage - 1
        })
    }

    // This function takes users to their desired page in the registration form.
    function gotoPage(index) {
        setCurrentPage(index)
    }

    return (
        <form onSubmit={(event) => { props.submission(event, currentPage); nextPage() }}>
            <h1 class="text-center text-2xl sm:mb-0 text-gray-600 font-bold font-sans"> Register </h1>

            {/* If any error needs to be displayed on the form, it is displayed here*/}
            {props.error ? <h3 class='text-center text-md text-red-800 font-medium font-serif mt-4'>{props.error}</h3> : ''}


            {/* A status bar rests at the top of registration form to easily switch between pages and to denote progress. */}
            <div class="flex justify-center sm:p-8 md:p-12 md:pb-8 mt-4 sm:mt-0">
                {props.fields.map((field, foo) => (
                    <div key={foo} class={foo !== 0 ? `w-full flex items-center text-gray-400 dark:text-white before:content-[''] before:w-full before:h-1 before:border-b before:border-gray-100 before:border-4 before:inline-block dark:before:border-blue-800 [&.active]:text-white  [&.active]:before:border-indigo-800 ${currentPage >= foo && 'active'}` : "text-white dark:text-white"}>
                        <div onClick={foo < currentPage ? () => { gotoPage(foo) } : () => ''} class={`${currentPage >= foo && 'active'} flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-blue-800 shrink-0  [&.active]:bg-indigo-800 [&.active]:hover:bg-indigo-600`}>{foo + 1}</ div>
                    </div>
                ))}
            </div>


            <div class="sm:grid grid-cols-2 gap-x-8 gap-y-2 sm:px-6 items-end">
                {/* Rendering every input field based on their type (through respective ids)*/}
                {props.fields[currentPage].map((input) => (
                    input.id <= 6 || [8, 9, 10, 11].includes(input.id) ?
                        <FormInput key={input.id} {...input} onChange={props.updation} updation={props.updation} value={props.values[input.name]} values={props.values} />
                        : input.id === 7 ?
                            <DropdownInput key={input.id} {...input} updation={props.updation} value={props.values[input.name]} />
                            : [12, 13].includes(input.id) ?
                                props.values["bp"] ?
                                    <FormInput key={input.id} {...input} onChange={props.updation} value={props.values[input.name]} />
                                    : ''
                                : input.id === 14 ?
                                    props.values["diabetes"] ?
                                        <FormInput key={input.id} {...input} onChange={props.updation} value={props.values[input.name]} />
                                        : ''
                                    :
                                    ''
                ))}
            </div>

            {/* For first page of the registration form, user is provided with an option to navigate to the Login Form.
              * For other pages, that option is replaced by a button to navigate to the previous page.
              */}
            <div class="flex justify-between items-end sm:px-6 pt-2">
                {currentPage === 0 ?
                    <div>
                        Already a member?
                        <p onClick={(e) => { e.preventDefault(); switchMenu("Register") }} class="cursor-pointer hover:text-indigo-800 hover:font-semibold"> Login here</p>
                    </div>
                    :
                    <div class="w-1/2.5 sm:w-1/5">
                        <Button placeholder="Skip" type="button" onClick={currentPage !== props.fields.length - 1 ? () => { nextPage(); props.skip(currentPage) } : (e) => { { props.skip(currentPage); props.submission(e, currentPage) } }} />
                    </div>
                }

                <div class="w-1/2.5 sm:w-1/5">
                    <Button placeholder={currentPage === props.fields.length - 1 ? "Submit" : "Next"} />
                </div>
            </div>
        </form>
    )
}


// This component is responsible for rendering input fields and...
// ...changes its type based on whether it's a checkbox, dropdown or other input (based on id).
function FormInput(props) {
    const { id, label, errorMessage, onChange, ...otherProps } = props

    // This state variable stores whether an input value is valid or not
    const [invalid, setInvalid] = React.useState(0)

    // Every time a user leaves an input field, this function is called to check the validity of entered input.
    function checkValid(e, idInvalid) {
        onChange(e)
        if (e.target.checkValidity()) setInvalid(0)
        else setInvalid(idInvalid)
    }

    // As the input type is currently decided based on id, the code looks quite messy.
    // It would be replaced by a field responsible for carrying category of input field in further updates.
    return (
        <div>
            {/*Everytime a new category of inputs show up because of a checkbox being checked, this statement helps them to highlight their category.*/}
            {props.id == 12 && <div class="text-xs text-gray-500 mt-5">Fill down your most-recent blood pressure information</div>}
            {props.id == 14 && <div class="text-xs text-gray-500 mt-5">Fill down your most-recent aspartate aminotransferase(AST) blood test information</div>}

            {// Do not display label for checkboxes as it will be displayed alonside checkbox.
                ![7, 10, 11, 19, 20, 21].includes(props.id) && <label class={props.id < 21 ? 'text-gray-800 font-semibold block mt-3 mb-2 text-md' : 'text-gray-600 font-semibold block mt-3 mb-2 text-sm'}>
                    {props.label}
                    {// Whenever invalid is true for an input(except checkbox), the error message is displayed here
                        props.id === invalid && <span class='text-red-800 text-sm font-medium font-serif'> ({errorMessage})</span>
                    }
                </label>
            }


            <div class={props.id > 6 ? ![7, 10, 11, 19, 20, 21].includes(props.id) ? 'flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus:ring-inset focus-within:ring-indigo-600 sm:max-w-md' : 'flex relative mt-2 rounded-lg items-center' : ''}>
                <input
                    class={props.id <= 6 ? 'w-full px-4 py-2 rounded-lg focus:outline-none border-gray-300 focus-within:ring-indigo-600' : [10, 11, 19, 20, 21].includes(props.id) ? 'h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-white cursor-pointer' : 'block w-full border-0 bg-transparent py-2 px-4 focus:ring-0 focus:ring-offset-0 sm:text-sm sm:leading-6'}
                    onChange={e => { checkValid(e, props.id) }}
                    {...otherProps} onBlur={e => checkValid(e, props.id)}
                />

                {// Display label next to checkboxes in case of checkbox.
                    [7, 10, 11, 19, 20, 21].includes(props.id) && <span class="pl-2 text-gray-800 font-semibold block text-md">{props.label}
                        {// Whenever invalid is true for a checkbox, the error message is displayed here
                            props.id === invalid && <span class='text-red-800 text-sm font-medium font-serif'>  ({errorMessage})</span>
                        }
                    </span>}


                {[8, 9].includes(props.id) ?
                    <DropdownInput id={props.id} {...otherProps} updation={props.updation} value={props.values} />
                    : [12, 13, 14].includes(props.id) || props.id > 21 ?
                        <span class='flex select-none items-center text-gray-500 sm:text-sm flex-shrink-0'>
                            {props.id > 21 && props.showRange ? <span class="flex select-none items-center text-gray-500 sm:text-sm flex-shrink-0">
                                <input class='flex rounded-md w-9 select-none text-center ml-3 mr-1 px-1 my-2 bg-red-900 hover:bg-red-700 text-white focus:outline-none text-xs' value={props.low[props.name]} onChange={(e) => props.updateRange(e, "low", props.name)}>
                                </input>
                                -
                                <input class='flex rounded-md w-9 select-none text-center ml-1 mr-3 px-1 my-2 bg-green-900 hover:bg-green-700 text-white focus:outline-none text-xs' value={props.high[props.name]} onChange={(e) => props.updateRange(e, "high", props.name)}>
                                </input>
                            </span> : <p class="pr-3">{props.placeholder}</p>}</span>
                        : ''}
            </div>
        </div>
    )
}


// This is the ground level component responsible for rendering every button.
function Button(props) {
    return (
        <button type={props.type} onClick={props.onClick} class='w-full mt-6 bg-indigo-800 hover:bg-indigo-600 rounded-lg px-4 py-2 text-center text-lg text-white tracing-wide font-semibold font-sans'>
            {props.placeholder}
        </button>
    )
}


// This is the ground level component responsible for rendering every dropdown.
function DropdownInput(props) {
    const { id, label, errorMessage, ...otherProps } = props

    // State variables for displaying the units of weight and height inputs
    const wUnits = ["kg", "lb"]
    const hUnits = ["in", "cm"]

    /* Rendering the country component which is reponsible for a dropdown list of countries*/
    if (props.id === 7) {

        // This state object stores list of countries fetched from the server
        const [country_list, getcountry_list] = React.useState({})

        // List of countries is fetched from the server. useEffect is used to avoid more than one iteration.
        React.useEffect(() => {
            fetch(`/country_list`, {
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
                },
            })
                .then(response => {
                    return response.json()
                })
                .then(list => {
                    getcountry_list(list)
                })
        }, []
        )

        return (
            <div>
                <label class='text-gray-800 font-semibold block mt-3 mb-2 text-md'>
                    {props.label}
                </label>
                <select class='w-full px-4 py-2 rounded-lg border-gray-300 focus-within:ring-indigo-600' {...otherProps}
                    onChange={props.updation} value={props.value}>
                    <option disabled value="">Select a country</option>
                    {Object.keys(country_list).map((countryCode) =>
                        <option value={countryCode}>{country_list[countryCode]}</option>
                    )}
                </select>
            </div>
        )
    }

    // Rendering height/weight units component facilitating users to pick their unit of choice.
    else return (
        <div class='inset-y-0 right-0 flex items-center'>
            <select name={props.id === 8 ? 'wUnit' : 'hUnit'}
                class='h-full rounded-lg border-none bg-transparent py-0 pl-2 pr-7 focus:ring-0'
                onChange={props.updation} value={props.id === 8 ? props.value['wUnit'] : props.value['hUnit']}>
                {props.id === 8 ?
                    wUnits.map((unit) => (
                        <option value={unit}>{unit}</option>
                    )) :
                    hUnits.map((unit) => (
                        <option value={unit}>{unit}</option>
                    ))
                }
            </select>
        </div>

    )
}


// This function is solely responsible for sending collected data to the server through fetch API
function sendToServer(formName, fields, setError) {
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Check which form is received
    if (formName === "Register") {

        // Weight and Height is converted into kilograms and centimetres respectively before sending to the server
        if (fields.wUnit === "lb") {
            fields.weight /= 2.2046
        }
        if (fields.hUnit === "in") {
            fields.height *= 2.54
        }

        fetch(`/authenticate`, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                formName: "Register",
                firstName: fields.firstName,
                lastName: fields.lastName,
                email: fields.email,
                dob: fields.dob,
                password: fields.password,
                confirmation: fields.confirmation,
                country: fields.country,
                weight: fields.weight,
                height: fields.height,
                bp: fields.bp,
                systolic: fields.systolic,
                diastolic: fields.diastolic,
                diabetes: fields.diabetes,
                ast: fields.ast
            })
        })
            .then(response => {
                if (response.redirected) {
                    // If response is supposed to be redirected, it indicates Success.
                    window.location.replace(response.url)
                }
                return response.json()
            }).then(message => {
                // If there is a message received, this indicates failure of submission.
                setError(message.message)
            })
    }

    else if (formName === "Login") {
        fetch(`/authenticate`, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                formName: "Login",
                email: fields.email,
                password: fields.password
            })
        })
            .then(response => {
                if (response.redirected) {
                    // If response is supposed to be redirected, it indicates Success.
                    window.location.replace(response.url)
                }
                return response.json()
            }).then(message => {
                // If there is a message received, this indicates failure of submission.
                setError(message.message)
            })
    }

    else if (formName === "Test") {
        if (fields.rangeStatus) {
            // Update new range of parameters.
            fetch(`/para_range`, {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({
                    low: fields.low,
                    high: fields.high
                })
            })
                .then(response => {
                    return response.json()
                }).then(message => {
                    // If message returned is "Success", this indicates sucessful updation of ranges.
                    if (message.message === "Success") {
                        // Submit test entries.
                        fetch(`/add`, {
                            method: 'POST',
                            credentials: 'same-origin',
                            headers: {
                                'Accept': 'application/json',
                                'X-Requested-With': 'XMLHttpRequest',
                                'X-CSRFToken': csrftoken
                            },
                            body: JSON.stringify({
                                formData: fields.formData
                            })
                        })
                            .then(response => {
                                // If response is supposed to be redirected, it indicates Success.
                                if (response.redirected) {
                                    window.location.replace(response.url)
                                }
                                return response.json()
                            }).then(message => {
                                // If there is a message received, this indicates failure of submission.
                                setError(message.message)
                            })
                    }
                    // If message returned is not "Success", this indicates failure during updation of ranges
                    else setError(message.message)
                })
        }
        else {
            // Submit test entries.
            fetch(`/add`, {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({
                    formData: fields.formData
                })
            })
                .then(response => {
                    // If response is supposed to be redirected, it indicates Success.
                    if (response.redirected) {
                        window.location.replace(response.url)
                    }
                    return response.json()
                }).then(message => {
                    // If there is a message received, this indicates failure of submission.
                    setError(message.message)
                })
        }
    }
}


// Whenever url points to the 'add' path, forms to enter test parameters need to be displayed.
if (window.location.pathname === '/add') {
    ReactDOM.render(<TestForm />, document.querySelector('#logged'))
}


/* This component aligns form fields of Form where test report can be enterred.
 * A checkbox exists allowing users to edit range of test parameters while entering test values.
 * Test Values are categorised into CBC, Vitamins and Minerals.
 * For submitting this form, atleast one off the above categories MUST be filled.
 */
function TestForm() {
    // All the inputs, when submitted through form, are stored in the following state object.
    // The ...status properties are initially false and are turned true whenever respective category's checkbox is checked.
    // If a category's checkbox is checked, atleast one of it's fields must be filled to bypass empty submission constraint.
    const [testInputs, setTestInputs] = React.useState({
        CBCStatus: false,
        Hb: "",
        PCV: "",
        RBC_count: "",
        MCV: "",
        MCH: "",
        MCHC: "",
        RDW: "",
        TLC: "",
        DLC_N: "",
        DLC_L: "",
        DLC_M: "",
        DLC_E: "",
        DLC_B: "",
        ALC_N: "",
        ALC_L: "",
        ALC_M: "",
        ALC_E: "",
        ALC_B: "",
        Platelets: "",
        MPV: "",

        vitStatus: false,
        A: "",
        B1: "",
        B2: "",
        B3: "",
        B5: "",
        B6: "",
        B7: "",
        B9: "",
        B12: "",
        C: "",
        D: "",
        E: "",
        K: "",

        minStatus: false,
        Ca: "",
        P: "",
        Mg: "",
        Zn: ""
    })

    // These objects will always be empty. They are used to validate empty form submissions
    const emptyCBCInputs = {
        CBCStatus: true,
        Hb: "",
        PCV: "",
        RBC_count: "",
        MCV: "",
        MCH: "",
        MCHC: "",
        RDW: "",
        TLC: "",
        DLC_N: "",
        DLC_L: "",
        DLC_M: "",
        DLC_E: "",
        DLC_B: "",
        ALC_N: "",
        ALC_L: "",
        ALC_M: "",
        ALC_E: "",
        ALC_B: "",
        Platelets: "",
        MPV: ""
    }
    const emptyVitInputs = {
        vitStatus: true,
        A: "",
        B1: "",
        B2: "",
        B3: "",
        B5: "",
        B6: "",
        B7: "",
        B9: "",
        B12: "",
        C: "",
        D: "",
        E: "",
        K: ""
    }
    const emptyMinInputs = {
        minStatus: true,
        Ca: "",
        P: "",
        Mg: "",
        Zn: ""
    }

    // HTML Input tag attributes for each form field, binded in separapte arrays for each category.
    // Notice that every category has a checkbox?
    // If a category's checkbox is checked, atleast one of it's fields must be filled to bypass empty submission constraint.
    const testInputFields = [

        {
            id: 19,
            label: "CBC",
            name: "CBCStatus",
            type: "checkbox"
        },
        {
            id: 20,
            label: "Vitamin",
            name: "vitStatus",
            type: "checkbox"
        },
        {
            id: 21,
            label: "Minerals",
            name: "minStatus",
            type: "checkbox"
        },
        {
            id: 22,
            name: "Hb",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in g/dL",
            label: "Haemoglobin",
            errorMessage: "Error"
        },
        {
            id: 23,
            name: "PCV",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in %",
            label: "PCV",
        },
        {
            id: 24,
            name: "RBC_count",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in mil/mm³",
            label: "RBC Count",
        },
        {
            id: 25,
            name: "MCV",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in fL",
            label: "Mean Corpuscular Volume",
        },
        {
            id: 26,
            name: "MCH",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in pg",
            label: "Mean Corpuscular Hemoglobin",
        },
        {
            id: 27,
            name: "MCHC",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in g/dL",
            label: "Mean Corpuscular Hemoglobin Concentration",
        },
        {
            id: 28,
            name: "RDW",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in %",
            label: "Red Cell Distribution Width",
        },
        {
            id: 29,
            name: "TLC",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in thou/mm³",
            label: "Total Leukocyte Count",
        },
        {
            id: 30,
            name: "DLC_N",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in %",
            label: "Differential Neutrophils Count",
        },
        {
            id: 31,
            name: "DLC_L",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in %",
            label: "Differential Lymphocytes Count",
        },
        {
            id: 32,
            name: "DLC_M",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in %",
            label: "Differential Monocytes Count",
        },
        {
            id: 33,
            name: "DLC_E",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in %",
            label: "Differential Eosinophills Count",
        },
        {
            id: 34,
            name: "DLC_B",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in %",
            label: "Differential Basophills Count",
        },
        {
            id: 35,
            name: "ALC_N",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in thou/mm³",
            label: "Absolute Neutrophills Count",
        },
        {
            id: 36,
            name: "ALC_L",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in thou/mm³",
            label: "Absolute Lymphocytes Count",
        },
        {
            id: 37,
            name: "ALC_M",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in thou/mm³",
            label: "Absolute Monocytes Count",
        },
        {
            id: 38,
            name: "ALC_E",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in thou/mm³",
            label: "Absolute Eosinophills Count",
        },
        {
            id: 39,
            name: "ALC_B",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in thou/mm³",
            label: "Absolute Basophills Count",
        },
        {
            id: 40,
            name: "Platelets",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in thou/mm³",
            label: "Platelets",
        },
        {
            id: 41,
            name: "MPV",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in fL",
            label: "Mean Platelet Volume",
        }
        ,

        {
            id: 42,
            name: "A",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin A",
        },
        {
            id: 43,
            name: "B1",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin B1(Thiamin)",
        },
        {
            id: 44,
            name: "B2",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin B2(Riboflavin)",
        },
        {
            id: 45,
            name: "B3",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin B3(Nicotinic Acid)",
        },
        {
            id: 46,
            name: "B5",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin B5(Pantothenic)",
        },
        {
            id: 47,
            name: "B6",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin B6(P5P)",
        },
        {
            id: 48,
            name: "B7",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin B7(Biotin)",
        },
        {
            id: 49,
            name: "B9",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin B9(Folic Acid)",
        },
        {
            id: 50,
            name: "B12",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin B12",
        },
        {
            id: 51,
            name: "C",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin C",
        },
        {
            id: 54,
            name: "D",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin D",
        },
        {
            id: 55,
            name: "E",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin E",
        },
        {
            id: 56,
            name: "K",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in ng/mL",
            label: "Vitamin K",
        }
        ,

        {
            id: 57,
            name: "Ca",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in mg/dL",
            label: "Calcium",
        },
        {
            id: 58,
            name: "P",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in mg/dL",
            label: "Phosphorus",
        },
        {
            id: 59,
            name: "Mg",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in mg/dL",
            label: "Magnesium",
        },
        {
            id: 60,
            name: "Zn",
            type: "number",
            min: "0",
            step: "0.001",
            placeholder: "in mcg/dL",
            label: "Zinc",
        }

    ]

    // Acts as an indicator for whether to display the range of parameters
    const [showRange, setShowRange] = React.useState(false)

    // State variables to store lower and upper range of parameters
    const [high, setHigh] = React.useState()
    const [low, setLow] = React.useState()

    // State variable to store range of each parameter when fetched from server,... 
    // ...for easily allocating them to low and high state objects later.
    const [range, setRange] = React.useState()

    // Get range of each parameter from the database(if not already)... 
    // ...and assigns them respectively to the low and high state objects.
    if (typeof range === 'undefined') getRange(setRange)
    else {
        const cbcUpper = range.cbc_upper
        const cbcLower = range.cbc_lower
        const vitminUpper = range.vitmin_upper
        const vitminLower = range.vitmin_lower

        if (typeof (low) === 'undefined') setLow(Object.assign(cbcLower, vitminLower))
        if (typeof (high) === 'undefined') setHigh(Object.assign(cbcUpper, vitminUpper))
    }

    // Update new ranges entered by the user unless they are invalid.
    // Invalid states(not limited to) a high(or low) range of a parameter isn't...
    // ...below(or exceeding) the current low(or high) range for that parameter.
    const updateRange = (e, type, name) => {
        if (type === "low") {
            if (e.target.value >= high[name]) alert("Lower can't be more than high")
            else setLow({ ...low, [name]: e.target.value })
        }
        if (type === "high") {
            if (e.target.value <= low[name]) alert("Higher can't be less than lower")
            else setHigh({ ...high, [name]: e.target.value })
        }
    }

    // Whenever a value for a test parameter is entered, update state object's property related to that parameter.
    // Also, if a checkbox related to category of test is (un)checked,... 
    // ...set it to (false)true thus displaying input form fields for it's parameters.
    const updateTestInputs = (e) => {
        if (e.target.type === "checkbox") {
            if (e.target.checked) setTestInputs({ ...testInputs, [e.target.name]: true })
            else setTestInputs({ ...testInputs, [e.target.name]: false })
        }
        else setTestInputs({ ...testInputs, [e.target.name]: e.target.value })
    }

    // Error message to be displayed if the form submission fails
    const [error, setError] = React.useState()

    // Function responsible for submission of test inputs and new ranges.
    const submitform = (e) => {
        e.preventDefault()

        // Empty test form-field values to validate the test form submisssion is not empty.
        const emptyCBC = JSON.stringify(emptyCBCInputs).slice(1, -1)
        const emptyVit = JSON.stringify(emptyVitInputs).slice(1, -1)
        const emptyMin = JSON.stringify(emptyMinInputs).slice(1, -1)
        const formData = JSON.stringify(testInputs)

        // Empty range form-field values to validate the range form submisssion is not empty.
        const cbcUpper = JSON.stringify(range.cbc_upper).slice(1, -1)
        const cbcLower = JSON.stringify(range.cbc_lower).slice(1, -1)
        const vitminUpper = JSON.stringify(range.vitmin_upper).slice(1, -1)
        const vitminLower = JSON.stringify(range.vitmin_lower).slice(1, -1)
        const highData = JSON.stringify(high)
        const lowData = JSON.stringify(low)

        /* fields Object is supposed to contain all the data expected to be sent to the server.
         * In max case, it will have the following properties:
         * - formData: Contains all the data(parameter values) about tests entered by the user.
         * - rangeStatus: Denotes whether the range values have been customised by the user. (if false, no data regarding range is sent to the server)
         * - low: Object containing new lower range values for all parameters. (Not checked if rangeStatusis false)
         * - high: Object containing new higher range values for all parameters. (Not checked if rangeStatusis false)
        
         * Since two different fetch(POST) requests are sent to the server,... 
         * ...one for test inputs(formData) and one for updating range... 
         * ...Avoiding the latter when no change in range is observed makes the process efficient.
         */
        const fields = { formData: testInputs, rangeStatus: false }


        // Validate if submitted values(formData) contain all empty fields for a category(CBC, Vitamin or Minerals),... 
        // ...yet have the respective ...Status property marked as true. This would indicate empty form submission for a checked category.
        if (formData.includes(emptyCBC) || formData.includes(emptyVit) || formData.includes(emptyMin)) alert("Cannot submit empty form")
        else {
            // Now that we know we don't have every field empty for any checked category,...
            // ...we can safely remove all empty fields to reduce API request's body size.
            for (const key in testInputs) {
                if (testInputs[key] === '') {
                    delete testInputs[key]
                }
            }
            if (highData.includes(cbcUpper) && lowData.includes(cbcLower) && lowData.includes(vitminLower) && highData.includes(vitminUpper)) {
                // If the Custom Range option was checked and no range value was customised, send only the test data to the server and notify user.
                if (showRange) {
                  alert("No change in range was observed");  
                }

                // Custom function responsible for carrying data to the server has following three arguments chronologically:
                // - "Test" denoting the API endpoint to be reached must be the one related to creating a new test report.
                // - Data to be sent
                // - In case of an Error, the callback function to display error.
                sendToServer("Test", fields, setError)
            }
            else {
                // Since it is confirmed that the range was modified, associate required parameters for successfully sending range...
                // ...to the server.
                fields['rangeStatus'] = true
                fields['low'] = low
                fields['high'] = high

                // Custom function responsible for carrying data to the server has following three arguments chronologically:
                // - "Test" denoting the API endpoint to be reached must be the one related to creating a new test report.
                // - Data to be sent
                // - In case of an Error, the callback function to display error.
                sendToServer("Test", fields, setError)
            }
        }
    }

    return (
        <form onSubmit={submitform} class="w-4/5 sm:w-2.5/3 bg-white rounded-lg shadow-lg p-10 m-10">
            <h1 onClick={redirectToHome} class="cursor-pointer text-center text-4xl sm:mb-0 text-gray-600 font-bold font-sans"> Test Tube Yum Yums </h1>

        {/* If any error needs to be displayed on the form, it is displayed here*/}
        {error && <h3 class='text-center text-md text-red-800 font-medium font-serif mt-2'>{error}</h3>}

            <div class="flex w-44 justify-center py-2 items-center rounded-3xl bg-gradient-to-r from-indigo-200 via-indigo-50 via-70% to-indigo-100 mt-6 mb-4">
                <input class="h-5 w-5 rounded border-0 text-gray-600 focus:border-0 focus:ring-offset-0 focus:ring-0 cursor-pointer" type="checkbox" onChange={(e) => { e.target.checked ? setShowRange(true) : setShowRange(false) }} />
                <span class="pl-2 text-gray-600 text-sm font-medium">View/Modify range</span>
            </div>

            <h1 class="text-xl text-gray-600 font-light font-sans sm:pl-8 md:pl-12 mt-4 sm:mt-0">Select test type and enter the values</h1>
            <div class="sm:grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-16 gap-y-8 items-end sm:p-8 md:p-12 md:pb-8 md:pt-3">
                {testInputFields.map((input) => (
                    [19, 20, 21].includes(input.id) ? <FormInput {...input} onChange={updateTestInputs} value={testInputs[input.name]} />
                        :
                        ((([22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41].includes(input.id) && (testInputs['CBCStatus'])) ||
                            ([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 54, 55, 56].includes(input.id) && (testInputs['vitStatus'])) ||
                            ([57, 58, 59, 60].includes(input.id) && (testInputs['minStatus']))
                        ) &&
                            <FormInput {...input} onChange={updateTestInputs} showRange={showRange} low={low} high={high} updateRange={updateRange} />)))
                }
                {(testInputs['CBCStatus'] || testInputs['vitStatus'] || testInputs['minStatus']) && <Button type="submit" placeholder="Submit" />}
            </div>
        </form>
    )
}

const redirectToHome = () => {
    window.location.href = "/";
};

function getRange(setRange) {
    // Get csrf token directly from html [UNSAFE FOR REAL-WORLD USAGE]
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Range of each parameter is fetched fromt the server. useEffect is used to avoid more than one iteration.
    fetch(`/para_range`, {
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
        },
    })
        .then(response => {
            return response.json()
        })
        .then(rangeDict => {
            // The received dictionary(rangeDict) contains four keys: cbc_upper, cbc_lower, vitmin_upper, vitmin_lower.
            // Values of them are again dictionaries with parameter's name and (lower/upper) range as key-value pairs.
            // Each value is converted from String to float and the updated rangeDict is assigned to Range state-object through callback.
            for (const key in rangeDict) {
                for (const childKey in rangeDict[key]) {
                    rangeDict[key][childKey] = parseFloat(rangeDict[key][childKey])
                    if (childKey === "id") delete rangeDict[key][childKey]
                }
            }
            setRange(rangeDict);
        })
}

/** 
 * The portion below would come in handy when showcasing individual food items through an overlay.
 * However, they are of no use for the current version.
*/

// function showFoodDetailOverlay(item) {
//     // Replace single quotes with double quotes
//     item = item.replace(/'/g, '"');
    
//     // Convert the string of item detail to a dictionary
//     item = JSON.parse(item)
//     document.querySelector('#overlay').setAttribute('class', 'block');
//     ReactDOM.render(<FoodDetailOverlay item={item} />, document.querySelector('#overlay'))
//     document.querySelector('#body').setAttribute('class', 'hidden');
// }

// function FoodDetailOverlay(props) {
//     const {item, ...otherProps} = props;
//     return (
//         <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-black bg-opacity-50">
//         <div className="bg-white p-8 max-w-md">
//           <h2 className="text-2xl font-bold mb-4">{item.name}</h2>
//           {/* Add other item details here */}
//           <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={closeFoodDetailOverlay}>Close</button>
//         </div>
//       </div>
//     );
// }

// function closeFoodDetailOverlay() {
//     document.querySelector('#overlay').setAttribute('class', 'hidden');
//     document.querySelector('#body').setAttribute('class', 'block');
// }