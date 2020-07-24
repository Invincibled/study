import React, {Component} from 'react';
import PubSub from 'pubsub-js'

class News extends Component {
    constructor(props) {
        super(props);
        this.state = {
            num : 123,
            ziText:"我是一个子组件向上传递"
        }
    }
    fun(){
        this.setState({
            num:321
        })
    }
    pubsub(){
        PubSub.publish("evt", this.state.num)
    }
    render() {
        return (
            <div>
                News---{this.props.text}---{this.state.num}
                <button onClick={this.fun.bind(this)}>点我</button>
                <button onClick={this.props.fufun.bind(this,this.state.ziText)}>啦啦啦</button>
                <button onClick={this.pubsub.bind(this)}>同级传输</button>
            </div>
        );
    }
}

export default News;