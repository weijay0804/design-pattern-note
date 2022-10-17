## 觀察者模式

> 定義物件之間的多對一依賴關係，當一個物件更新狀態時，依賴他的物件都會收到通知與更新

### 鬆耦合 (loosely coupled)
* 觀察者模式是一種鬆耦合， subject 只知道觀察者實作了某個介面，不需要知道觀察著的具體類別
* 可以隨時加入新的觀察者
* 如果要加入新的觀察者類型，不需要修改 subject
* 可以重複利用 subject 或觀察者，又不會影響對方

### 觀察者模式 UML
![UML](/Chapter2-Observer/docs/observer.png)

### 實際例子
![UML](/Chapter2-Observer/docs/weather-station.png)