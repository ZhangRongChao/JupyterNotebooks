
/*
 Swift中的协议相当于其它编程语言中的接口。协议定义了属性、方法、下标和构造器等必须满足特定要求的规范。协议并不提供这些要求的具体实现，而是仅仅描述这些实现需要遵守的规范。结构体、类和枚举类型都可以为某个协议定义的属性要求、方法要求、下标要求和构造器要求等提供具体实现，从而成为该协议的遵守者（实现者）。
 
 定义协议的语法格式为：
 protocol SomeProtocol {
    // 属性要求、方法要求、下标要求和构造器要求等
 }
 
 如果想让结构体、类或枚举类型遵守某个协议，可以在声明类型时在类型名的后面加上协议名，中间用冒号分隔；如果同时遵守多个协议，多个协议之间用逗号分隔。其语法格式为：
 struct|class|enum SomeType: FirstProtocol, SecondProtocol, ThirdProtocol {
    // 类型的定义，包括指定协议的所有要求的具体实现
 }
 
 如果想让某个类在继承的同时遵守协议，在声明该类时必须将父类名放在协议名之前，中间用逗号分隔，其语法格式为：
 class SomeClass: SuperClass, FirstProtocol, SecondProtocol {
    // 类的定义
 }
 */
