//在PreviewKeyDown事件中检测按键按下
private void Form1_PreviewKeyDown(object sender, PreviewKeyDownEventArgs e){
    switch (e.KeyValue){
        case 'A':
            if (key1down == false)
                    MessageBox.Show("A down");
                    key1down = true;             // 按键"A"按下此标志为true，直到放开
                    break;
        case 'B':
            if (key2down == false)
                MessageBox.Show("B down");
                key2down = true;            // 按键"B"按下此标志为true，直到放开
                break;
        case 'C':
            if (key3down == false)
                MessageBox.Show("C down");
                key3down = true;            // 按键"C"按下此标志为true，直到放开
                break;
        
    }
    
}
 
//在KeyUp事件中检测按键放开：
private void Form1_KeyUp(object sender, KeyEventArgs e){
    switch (e.KeyValue){
        case 'A':
            MessageBox.Show("A up");
            key1down = false;           // 按键"A"放开此标志为false
            break;
        case 'B':
            MessageBox.Show("B up");
            key2down = false;          // 按键"A"放开此标志为false
            break;
        case 'C':
            MessageBox.Show("C up");
            key3down = false;          // 按键"A"放开此标志为false
            break;
        
    }
    
}

