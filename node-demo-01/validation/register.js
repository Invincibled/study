const Validator = require('validator')
const isEmpty = require('./is-empty')
module.exports = function validateRegisterInput(data) {

    let errors ={}

    if (!Validator.isLength(data.name, {min:2, max:30})){
        errors.name = "名字的长度不能小于2位数且不能超过30位";
    }
    if(Validator.isEmpty(data.name)){
        errors.name = " 名字不能为空"
    }
    if (Validator.isEmpty(data.email)){
        errors.email = "邮箱不能为空"
    }
    if (Validator.isEmpty(data.password)){
        errors.password = "密码不能为空"
    }
    if (!Validator.isLength(data.password, {min:6, max:30})){
        errors.password = "密码的长度不能小于6位数且不能超过30位";
    }
    if (!Validator.isEmail(data.email)){
        errors.email = "邮箱不合法"
    }

    return {
        errors,
        isValid:isEmpty(errors)
    }
}