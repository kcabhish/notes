# 7 important pillers in Angular Architecture

1. Template: The HTML view of Angular
2. Component: Binds the View and Model.
3. Modules: Groups components logically.
4. Bindings: Defines how view and component communicate.
5. Directive: Changes the HTML DOM behaviour.
6. Services: Helps to shre common logic across the project.
7. DI: Depndency injection helps to inject instance across constructor.

# Inteview Questions

## What are directives in Angular and how many types of directives exists?

Directives help you to attach behaviour in the HTML DOM. For example in the below code “ngModel” is a directive which when attached to the textbox binds the text box value to “myvariable”. <input [(ngModel)]="myvariable" type="text" value=""><br>
There are three types of directives in Angular :-
• Structural directives: - Change the DOM layout by adding and removing elements.
For example in the below code we have the “*ngFor” loop which is a example of structural directive. How many HTML table “tr” will be added in the HTML DOM layout depends on rows in the “coll” collection. 
```javascript
<tr *ngFor="let temp of coll"> <td>{{temp.CustomerName}}</td> </tr>
```
• Attribute directives: - Change the appearance and behaviour of HTML elements.
```javascript
<div [hidden]="Hide()">Some text</div>
```
• Component directives: - Directives with templates. It’s like a user control.

<my-grid [grid-data]="SalesModelObjs" </my-grid>
---

## Explain ViewChild and ViewChildren ?
## ViewChild vs ViewChildren vs ContentChild vs ContentChildren?

- ViewChild helps to reference view objects in the component to which it is connected.
- View Child references one object while ViewChildren references collection.
---
## Why do we need Templatereference variables?
- A template reference variable is used to give reference to a DOM Element, a component, directive, or a web component within a template.

### Parent Component
```
@Component({
  template: `
    <app-child #taskChild></app-child>
    <button (click)="triggerChild()">Start Child Task</button>
  `
})
export class ParentComponent {
  // Select the child using its template reference variable
  @ViewChild('taskChild') childRef!: ChildComponent;

  triggerChild() {
    this.childRef.startTask(); // Directly calling the child's method
  }
}

```
### Child Component
```
@Component({
  selector: 'app-child',
  template: `<p>Status: {{ status }}</p>`
})
export class ChildComponent {
  status = 'Idle';

  // Method to be called by parent
  startTask() {
    this.status = 'Processing...';
  }
}

```
---
## What is ContentProjection?
When you want to pass html contents form 1 component to component 2. This is similar to children in react.
- <ng-content>This is like children in react</ng-content>
## Explain Content projection Slot?
- you can pass in multiple <ng-content> into an html template using select='content-label'.
```
<!-- layout.component.html -->
<header>
  <ng-content select="[header]"></ng-content>
</header>
<main>
  <ng-content></ng-content> <!-- Default -->
</main>
<footer>
  <ng-content select="footer-links"></ng-content>
</footer>

<!-- Usage -->
<app-layout>
  <h1 header>Page Title</h1>
  <p>Main body content.</p>
  <footer-links>Link 1, Link 2</footer-links>
</app-layout>
```
## What is ContentChild and ContentChildren?
Similar to viewChild and viewChildren but in reverse. This is used to reference the contents that is being projected from parent to child. ViewChild 

# Component Life Cycles

## Explain the importance of Component life Cycle ?

constructor()
ngOnChanges()
ngOnInit()
ngDoCheck()
ngAfterContentInit()
ngAfterContentChecked()
ngAfterViewInit()
ngAfterViewChecked()
ngOnChanges()
ngOnDestroy()
ngDestroy()

## Explain events and sequence of component life cycle ?
## Constructor vs ngOnInit() ?

# HTTP Calls 

## what are angular pipes

- It helps transform angular expression from one form to another.
example Hello {{'world' | uppercase }} returns Hello WORLD