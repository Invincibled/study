const JwtStrategy = require('passport-jwt').Strategy,
  ExtractJwt = require('passport-jwt').ExtractJwt;
const keys = require('keys')
const mongoose = require('mongoose')
const User = require('../model/User')

const opts = {}
opts.jwtFromRequest = ExtractJwt.fromAuthHeaderAsBearerToken();
opts.secretOrKey = keys.secureOrKey;

module.exports = passport => {
    passport.use(new JwtStrategy(opts, async function(jwt_payload, done) {
       console.log(jwt_payload)
        const  user = User.findById(jwt_payload.id)
        if (user){
            return done(null, user)
        }
        return done(null, false);
    }));
}