const isEmpty = error=>{
    return error == undefined || error === null || (typeof error == 'object' && Object.keys(error).length ===0) || (typeof error == 'string' && error.trim().length === 0)
}

module.exports = isEmpty