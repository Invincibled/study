import React, {Component} from 'react';
import PubSub from 'pubsub-js'
class Phone extends Component {

    constructor(props) {
        super(props);
        this.state={
            text:"嘿嘿"
        }
        PubSub.subscribe("evt",(msg,data)=>{
            console.log(data)
        })
    }
    render() {
        return (
            <div>
                我是phone

            </div>
        );
    }
}

export default Phone;