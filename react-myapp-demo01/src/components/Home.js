import React, {Component, Fragment} from 'react';
// import ImgA from '../assets/1.jpg'
import News from './News'
import Phone from './Phone'
import Remote from "./Remote";
class Home extends Component {
    constructor(props) {
        super(props);
        this.state={
            context:"ffff"
        }

    }
    dataFun(text){
        console.log(text)
    }
    render() {
        return (
            <Fragment>
                <div>我是组建1</div>
                <News text={this.state.context} fufun={this.dataFun.bind(this)}/>
                <Phone />
                <Remote />
            </Fragment>
        );
    }
}

export default Home;