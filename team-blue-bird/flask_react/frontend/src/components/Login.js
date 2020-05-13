import React from "react";
import { Form, Input, Button, Checkbox } from 'antd';
import "../styles/Login.css";
import TopNavBar from "./TopNavBar"

const layout = {
    labelCol: {
        span: 8,
    },
    wrapperCol: {
        span: 16,
    },
};
const tailLayout = {
    wrapperCol: {
        offset: 8,
        span: 16,
    },
};
class Login extends React.Component{
    constructor(props) {
        super(props);
        this.handleClickBtn = this.handleClickBtn.bind(this);
    }
    handleClickBtn(){
        this.props.history.push("/")
    }
    render() {
        // const onFinish = values => {
        //     console.log('Success:', values);
        // };
        //
        // const onFinishFailed = errorInfo => {
        //     console.log('Failed:', errorInfo);
        // };
        return (
            <div>
                <TopNavBar />
                <Form
                    {...layout}
                    name="basic"
                    initialValues={{ remember: true }}
                    className="login-form"
                >
                    <Form.Item
                        label="Username"
                        name="username"
                        rules={[{ required: true, message: 'Please input your username!' }]}
                    >
                        <Input placeholder="Username"/>
                    </Form.Item>

                    <Form.Item
                        label="Password"
                        name="password"
                        rules={[{ required: true, message: 'Please input your password!' }]}
                    >
                        <Input.Password placeholder="Password"/>
                    </Form.Item>

                    <Form.Item {...tailLayout} name="remember" valuePropName="checked">
                        <Checkbox>Remember me</Checkbox>
                    </Form.Item>

                    <Form.Item {...tailLayout}>
                        <Button onClick={this.handleClickBtn} className="login-form-button" Type="primary" htmlType="submit">
                            Submit
                        </Button>
                    </Form.Item>
                </Form>
            </div>
        );
    };
}
export default Login;