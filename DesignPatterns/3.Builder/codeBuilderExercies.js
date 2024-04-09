class CodeBuilder
{
  constructor(className)
  {
    this.className = className;
    this.fields = [];
  }

  addField(name)
  {
    this.fields.push(name);
    return this;
  }

  generateFields() {
    const tempFields = [];
    this.fields.forEach(item => {
      tempFields.push(`\n        this.${item} = ${item}`);
    });
    return tempFields.join(';');
  }

  generateConstructor() {
    if (this.fields.length > 0) {
      return `constructor(${this.fields.join(', ')}) {`
    }
    return `constructor() {`
  }

  toString()
  {
    return `class ${this.className} {
    ${this.generateConstructor()}` +
    this.generateFields() +
    `
    }
  }
    `
  }
}

let cb = new CodeBuilder('Person');
cb.addField('name').addField('age');
console.log(cb.toString());