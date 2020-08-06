const encode = new TextEncoder()

const greetText = encode.encode("hello world\n my name is summer")


await Deno.writeFile("greet.txt", greetText)