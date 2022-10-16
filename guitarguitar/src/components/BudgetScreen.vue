<template>
<div>
    <h1>What is your budget?</h1>
    
    <div class="budgetSelector">
    <p>100</p>
    <RangeSelector/>
    <p>3000</p>
    </div>
    <button>Get My Guitar</button>
</div>
</template>
<script>
import RangeSelector from './RangeSelector.vue'
export default{
name: 'BudgetScreen',
component:{
    RangeSelector,
}
}
</script>