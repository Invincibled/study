import React, {Component} from 'react';
import axios from 'axios'
class Remote extends Component {

    constructor(props) {
        super(props);
        this.state={
            arr:[]
        }
    }

    componentDidMount() {
        this.ajaxFun()
    }
    ajaxFun(){
        axios.get("http://localhost:4000/arr").then((ok)=>{
            console.log(ok)
            this.setState({
                arr:ok.data
            })
        })
    }
    render() {
        return (
            <div>
                {this.state.arr.map((v,i)=>{
                    return <p key={v.id}>{v.name}</p>
                })}
            </div>
        );
    }
}

export default Remote;