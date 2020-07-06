var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var str = "111";
var str1 = "2222";
var str3 = "333";
var str4 = "fadfa";
var Flag;
(function (Flag) {
    Flag[Flag["success"] = 1] = "success";
    Flag[Flag["error"] = -1] = "error";
})(Flag || (Flag = {}));
var num;
console.log(num);
function remainParm(a, b) {
    var result = [];
    for (var _i = 2; _i < arguments.length; _i++) {
        result[_i - 2] = arguments[_i];
    }
    var sum = 0;
    for (var i = 0; i < result.length; i++) {
        sum += result[i];
    }
    return sum;
}
remainParm(1, 2, 3, 4, 5);
function f1() {
    return function (target) {
        console.log(target);
        console.log("装饰器1");
    };
}
function f2() {
    return function (target) {
        console.log(target);
        console.log("装饰器2");
    };
}
var Decrator = /** @class */ (function () {
    function Decrator() {
    }
    Decrator = __decorate([
        f1(),
        f2()
    ], Decrator);
    return Decrator;
}());
var api;
var d = Decrator();
console.log(d);
//# sourceMappingURL=index.js.map